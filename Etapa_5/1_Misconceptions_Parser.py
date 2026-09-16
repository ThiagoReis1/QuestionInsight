from VisitorMC3 import *
import ast
import os
import pandas as pd
from collections import defaultdict
import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import multiprocessing
import time
import sys
import json
from pathlib import Path
from tqdm import tqdm

# Caminhos
csv_questoes = "../Etapa_3/output/questoes_ordenadas.csv"
indice_usuarios_path = "../Etapa_3/output/indice_usuarios.json"
base_usuarios_path = "../Etapa_2/output/referencias_processamento.json"
output_summary = "output/misconceptions_resumo_por_questao.csv"
output_detailed = "output/misconceptions_detalhado_por_usuario.csv"
os.makedirs("output", exist_ok=True)

def carregar_referencias(path):
    references_path = Path(path).resolve()
    data = json.loads(references_path.read_text(encoding='utf-8'))
    source_root = Path(data['source_root'])
    if not source_root.is_absolute():
        source_root = (references_path.parent / source_root).resolve()
    data['_source_root'] = str(source_root)
    data['_users_by_id'] = {str(record.get('id')): record for record in data.get('users', [])}
    return data


def iterar_arquivos_usuario(data, user_id, kind, suffix=None):
    source_root = Path(data['_source_root'])
    record = data.get('_users_by_id', {}).get(str(user_id))
    if record is None:
        return
    for item in record.get('files', {}).get(kind, []):
        path = source_root / item['path']
        if path.is_file() and (suffix is None or path.name.endswith(suffix)):
            yield path

# Constants for MC³ detection
C4_MAX_ALLOWED_RANGEITER = 50
E2_MAX_ALLOWED_LISTS = 5
G4_MIN_VAR_CHRS = 4
G4_MIN_FNC_CHRS = 8
G4_MAX_ALLOWED_NONSIGNIFICANT = 70

MAX_WORKERS = max(1, min(int(os.environ.get('MC3_WORKERS', multiprocessing.cpu_count() or 1)), 8))
EXECUTOR_KIND = os.environ.get('MC3_EXECUTOR', 'process').strip().lower()

MC3_TYPES = [
    'A2', 'A3', 'A4', 'A5',
    'B4', 'B6', 'B8', 'B9', 'B10', 'B11', 'B12',
    'C1', 'C2', 'C3', 'C4', 'C8',
    'D4',
    'E1', 'E2',
    'G4', 'G5',
    'H1'
]

output_lock = threading.Lock()
thread_status = {}
completed_questions = set()
status_lock = threading.Lock()


indice_arquivos = {}  # {(usuario_id, questao_id): filepath}


def construir_indice(indice_usuarios_path, base_usuarios_path):
    """Indexa os códigos já filtrados por usuário e questão, sem copiá-los."""
    global indice_arquivos
    data = carregar_referencias(base_usuarios_path)
    indice = {}
    total = 0
    for registro in data.get('users', []):
        usuario_id = str(registro['id'])
        for filepath in iterar_arquivos_usuario(data, usuario_id, 'codes', '.py'):
            question_id = filepath.stem.rsplit('_', 1)[-1]
            if question_id:
                indice[(usuario_id, question_id)] = str(filepath)
                total += 1
    indice_arquivos = indice
    print(f"Índice construído: {total:,} arquivos referenciados ({len(data.get('users', [])):,} usuários)")


def inicializar_worker(indice):
    """Instala o índice em cada worker; funciona com fork e Windows spawn."""
    global indice_arquivos
    indice_arquivos = indice


def atualizar_status_thread(thread_id, questao_id, status):
    with status_lock:
        thread_status[thread_id] = {
            'questao_id': questao_id,
            'status': status,
            'timestamp': time.time()
        }

def marcar_questao_concluida(questao_id):
    with status_lock:
        completed_questions.add(questao_id)

def obter_status_threads():
    with status_lock:
        return dict(thread_status), set(completed_questions)


def analisar_codigo(filepath):
    """Analisa um arquivo Python e retorna os MC³ detectados."""
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            code = file.read()
        if not code or len(code.strip()) == 0:
            return []
        parsed = ast.parse(code)
    except Exception:
        return []

    visitor = VisitorMC3()

    try:
        res_map = {
            'A2': visitor.getA2(parsed),
            'A3': visitor.getA3(parsed),
            'A4': visitor.getA4(parsed),
            'A5': visitor.getA5(parsed),
            'B4': visitor.getB4(parsed),
            'B6': visitor.getB6(parsed),
            'B8': visitor.getB8(parsed),
            'B9': visitor.getB9(parsed),
            'B10': visitor.getB10(parsed),
            'B11': visitor.getB11(parsed),
            'B12': visitor.getB12(parsed),
            'C1': visitor.getC1(parsed),
            'C2': visitor.getC2(parsed),
            'C3': visitor.getC3(parsed),
            'C4': visitor.getC4(parsed, C4_MAX_ALLOWED_RANGEITER),
            'C8': visitor.getC8(parsed),
            'D4': visitor.getD4(parsed),
            'E1': visitor.getE1(parsed),
            'E2': visitor.getE2(parsed, E2_MAX_ALLOWED_LISTS),
            'G4': visitor.getG4(parsed, G4_MIN_VAR_CHRS, G4_MIN_FNC_CHRS, G4_MAX_ALLOWED_NONSIGNIFICANT),
            'G5': visitor.getG5(parsed),
            'H1': visitor.getH1(parsed),
        }

        # Normaliza tuplas (A4, A5) → bool e filtra os detectados
        return [mc for mc, res in res_map.items()
                if (res[0] if isinstance(res, tuple) else res)]

    except Exception:
        return []


def processar_questao(questao_data):
    """
    Processa uma questão: para cada aluno que a respondeu,
    busca O(1) no índice o arquivo {prova}_{questao}.py
    e analisa apenas ele.
    """
    questao_id, usuarios_str = questao_data
    questao_id_str = str(questao_id)
    thread_id = threading.current_thread().name

    atualizar_status_thread(thread_id, questao_id, "iniciando")

    usuarios = [u.strip() for u in usuarios_str.split(',')]

    mc3_counters = defaultdict(int)
    detailed_results = []

    atualizar_status_thread(thread_id, questao_id, "analisando_usuarios")

    for i, usuario_id in enumerate(usuarios):
        if i % 10 == 0:
            atualizar_status_thread(thread_id, questao_id, f"usuario_{i+1}/{len(usuarios)}")

        # O(1) — lookup direto no índice, sem tocar o disco
        filepath = indice_arquivos.get((str(usuario_id), questao_id_str))

        if filepath is None:
            continue  # aluno não tem arquivo para essa questão

        misconceptions = set(analisar_codigo(filepath))

        detailed_results.append({
            'question': questao_id,
            'usuario': usuario_id,
            'misconceptions_detectados': ','.join(sorted(misconceptions)),
            'total_misconceptions': len(misconceptions),
            'categorias_afetadas': len(set(mc[0] for mc in misconceptions))
        })

        for mc3 in misconceptions:
            mc3_counters[mc3] += 1

    atualizar_status_thread(thread_id, questao_id, "finalizando")

    summary_row = {'question': questao_id, 'respostas': len(usuarios)}
    for mc3_type in MC3_TYPES:
        summary_row[mc3_type] = mc3_counters[mc3_type]

    marcar_questao_concluida(questao_id)
    atualizar_status_thread(thread_id, questao_id, "concluida")

    return summary_row, detailed_results, mc3_counters


def gerar_relatorio_misconceptions():
    misconceptions_info = {
        'A2': 'Variável atribuída a si mesma',
        'A3': 'Variável inicializada desnecessariamente',
        'A4': 'Redefinição de built-in',
        'A5': 'Importação não utilizada',
        'B4': 'Comandos repetidos dentro de blocos if-elif-else',
        'B6': 'Comparação booleana tentada com loop while',
        'B8': 'Não utilização de elif/else',
        'B9': 'elif/else retestando condições já verificadas',
        'B10': 'elif/else desnecessário',
        'B11': 'Ifs distintos com blocos idênticos',
        'B12': 'Declarações if consecutivas iguais com operações distintas',
        'C1': 'Condição while testada novamente dentro do seu bloco',
        'C2': 'Loop redundante ou desnecessário',
        'C3': 'Operações redundantes dentro do loop',
        'C4': 'Número arbitrário de execuções de for loop ao invés de while',
        'C8': 'Loop for com sua variável de iteração sobrescrita',
        'D4': 'Variável fora do escopo da função',
        'E1': 'Verificação desnecessária de todas as combinações possíveis',
        'E2': 'Uso redundante ou desnecessário de listas',
        'G4': 'Funções/variáveis com nomes não significativos',
        'G5': 'Organização arbitrária de declarações',
        'H1': 'Declaração sem efeito'
    }
    print("\n" + "="*80)
    print("TIPOS DE MISCONCEPTIONS DETECTADOS (MC³)")
    print("="*80)
    for categoria in ['A', 'B', 'C', 'D', 'E', 'G', 'H']:
        print(f"\n--- Categoria {categoria} ---")
        for mc3_type in MC3_TYPES:
            if mc3_type.startswith(categoria):
                print(f"  {mc3_type}: {misconceptions_info[mc3_type]}")


def salvar_resultados_thread_safe(summary_data, detailed_data):
    with output_lock:
        print(f"\n💾 Salvando resultados...")
        pd.DataFrame(summary_data).to_csv(output_summary, index=False, encoding='utf-8')
        pd.DataFrame(detailed_data).to_csv(output_detailed, index=False, encoding='utf-8')
        print(f"✅ Arquivos salvos: {output_summary}, {output_detailed}")


def mostrar_status_threads():
    current_status, completed = obter_status_threads()
    print("\n" + "="*60)
    print("📊 STATUS DAS THREADS")
    print("="*60)
    for thread_id, info in current_status.items():
        status_emoji = {
            'iniciando': '🚀', 'analisando_usuarios': '🔍',
            'finalizando': '🔧', 'concluida': '✅'
        }.get(info['status'].split('_')[0], '⚙️')
        timestamp = time.strftime('%H:%M:%S', time.localtime(info['timestamp']))
        print(f"{status_emoji} {thread_id}: Questão {info['questao_id']} - {info['status']} ({timestamp})")
    if completed:
        print(f"\n✅ Questões concluídas ({len(completed)}): {sorted(list(completed))}")
    print("="*60)


def main():
    inicio_tempo = time.time()
    show_progress_bar = len(sys.argv) > 1 and sys.argv[1] == 'progressBar'

    if not show_progress_bar:
        gerar_relatorio_misconceptions()

    # ÍNDICE GLOBAL — varre o disco UMA única vez
    print(f"\n🔍 Construindo índice de arquivos...")
    construir_indice(indice_usuarios_path, base_usuarios_path)

    if not show_progress_bar:
        print(f"\nLendo questoes_ordenadas.csv...")
    df_questoes = pd.read_csv(csv_questoes)
    total_questoes = len(df_questoes)

    if show_progress_bar:
        print(f"🎯 Iniciando análise de {total_questoes} questões com {MAX_WORKERS} workers...")
    else:
        print(f"Configuração: {MAX_WORKERS} workers ({EXECUTOR_KIND}) para {total_questoes} questões")

    questoes_para_processar = list(
        df_questoes[['id', 'usuarios_respondidos']].itertuples(index=False, name=None)
    )

    summary_data = []
    detailed_data = []
    global_mc3_counts = defaultdict(int)

    if show_progress_bar:
        pbar = tqdm(total=total_questoes, desc="📈 Processando questões",
                    unit="questões", ncols=100, colour='green')

    if not show_progress_bar:
        print(f"\nIniciando processamento paralelo...")

    # ------------------------------------------------------------------
    # CORREÇÃO: status_monitor controlado por threading.Event em vez de
    # checar a variável local `questoes_processadas`, que não era
    # protegida por lock e podia ser lida em estado inconsistente pela
    # thread daemon, causando prints extras após o fim do processamento.
    # O Event.set() ao final do loop garante parada limpa e determinista.
    # ------------------------------------------------------------------
    stop_monitor = threading.Event()

    if not show_progress_bar and EXECUTOR_KIND == 'thread':
        def status_monitor():
            # Aguarda 5 segundos ou até receber o sinal de parada
            while not stop_monitor.wait(timeout=5):
                mostrar_status_threads()

        threading.Thread(target=status_monitor, daemon=True).start()

    questoes_processadas = 0

    executor_cls = ThreadPoolExecutor if EXECUTOR_KIND == 'thread' else ProcessPoolExecutor
    executor_kwargs = {'max_workers': MAX_WORKERS}
    if executor_cls is ProcessPoolExecutor:
        executor_kwargs.update({
            'initializer': inicializar_worker,
            'initargs': (indice_arquivos,),
        })
    else:
        executor_kwargs['thread_name_prefix'] = 'MC3-Worker'

    with executor_cls(**executor_kwargs) as executor:
        future_to_questao = {
            executor.submit(processar_questao, q): q[0]
            for q in questoes_para_processar
        }

        for future in as_completed(future_to_questao):
            questao_id = future_to_questao[future]
            try:
                summary_row, detailed_results, mc3_counters = future.result()
                summary_data.append(summary_row)
                detailed_data.extend(detailed_results)
                completed_questions.add(questao_id)
                for mc3, count in mc3_counters.items():
                    global_mc3_counts[mc3] += count
                questoes_processadas += 1
                if show_progress_bar:
                    pbar.set_postfix({
                        'Questão': questao_id,
                        'Concluídas': f"{questoes_processadas}/{total_questoes}",
                        'MC³': sum(mc3_counters.values())
                    })
                    pbar.update(1)
            except Exception as e:
                questoes_processadas += 1
                if show_progress_bar:
                    pbar.set_postfix({'Erro': f"Questão {questao_id}"})
                    pbar.update(1)
                else:
                    print(f"❌ Erro ao processar questão {questao_id}: {e}")

    # Sinaliza ao monitor que o processamento terminou — sem race condition
    stop_monitor.set()

    if show_progress_bar:
        pbar.close()
        print("\n📋 STATUS FINAL:")
        for thread_id in obter_status_threads()[0]:
            print(f"  {thread_id}: ✅ Finalizada")
        print(f"  📊 Total processado: {len(completed_questions)} questões")

    summary_data.sort(key=lambda row: int(row['question']))
    detailed_data.sort(key=lambda row: (int(row['question']), str(row['usuario'])))
    salvar_resultados_thread_safe(summary_data, detailed_data)

    tempo_total = time.time() - inicio_tempo
    print("\n" + "="*80)
    print("🎉 RELATÓRIO FINAL DE ANÁLISE")
    print("="*80)
    print(f"⏱️  Tempo total: {tempo_total:.2f} segundos")
    print(f"🔧 Threads: {MAX_WORKERS}")
    print(f"📊 Questões: {len(summary_data)}")
    print(f"👥 Análises: {len(detailed_data)}")

    if summary_data:
        total_usuarios_analisados = len(detailed_data)
        usuarios_com_misconceptions = sum(1 for r in detailed_data if r['total_misconceptions'] > 0)

        print(f"\n📈 ESTATÍSTICAS:")
        print(f"  👥 Usuários analisados: {total_usuarios_analisados:,}")
        print(f"  ⚠️  Com misconceptions: {usuarios_com_misconceptions:,}")
        print(f"  📊 Percentual: {round(usuarios_com_misconceptions/total_usuarios_analisados*100, 2)}%")
        print(f"  ⚡ Velocidade: {total_usuarios_analisados/tempo_total:.1f} usuários/seg")

        if not show_progress_bar:
            print(f"\n🏆 TOP 10 MC³:")
            for i, (mc3, count) in enumerate(
                sorted(global_mc3_counts.items(), key=lambda x: x[1], reverse=True)[:10], 1):
                print(f"  {i:2d}. {mc3}: {count:,} ({round(count/total_usuarios_analisados*100,2)}%)")

            print(f"\n📋 POR CATEGORIA:")
            for categoria in ['A', 'B', 'C', 'D', 'E', 'G', 'H']:
                cat_total = sum(global_mc3_counts[mc] for mc in MC3_TYPES if mc.startswith(categoria))
                if cat_total > 0:
                    print(f"  {categoria}: {cat_total:,} ({round(cat_total/total_usuarios_analisados*100,2)}%) "
                          f"- {len([m for m in MC3_TYPES if m.startswith(categoria)])} tipos")


if __name__ == "__main__":
    main()