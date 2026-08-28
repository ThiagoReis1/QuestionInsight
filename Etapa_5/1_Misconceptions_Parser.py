from VisitorMC3 import *
import ast
import os
import pandas as pd
from collections import defaultdict
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import sys
from tqdm import tqdm

# Caminhos
csv_questoes = "../Etapa_3/questoes_ordenadas.csv"
pasta_usuarios = "../Etapa_3/Processamento/UsuariosProcessamento"
output_summary = "misconceptions_summary_por_questao.csv"
output_detailed = "misconceptions_detailed_por_usuario.csv"

# Constants for MC³ detection
C4_MAX_ALLOWED_RANGEITER = 50
E2_MAX_ALLOWED_LISTS = 5
G4_MIN_VAR_CHRS = 4
G4_MIN_FNC_CHRS = 8
G4_MAX_ALLOWED_NONSIGNIFICANT = 70

# ------------------------------------------------------------------
# ELEGIBILIDADE ESTRUTURAL PARA B4/B8/B9
# ------------------------------------------------------------------
# B4, B8 e B9 só podem ocorrer em código que usa if/elif/else. Não há
# gabarito/solução de referência disponível — a elegibilidade de cada
# questão é derivada agregando, sobre as próprias submissões dos alunos
# daquela questão, a proporção de códigos que usam algum condicional.
# Se essa proporção for >= ELEGIBILIDADE_MIN_PROPORCAO_IF, a questão é
# marcada como estruturalmente elegível para B4/B8/B9 — ou seja, o
# grupo de comparação passa a ser "questões que podiam ter B4 mas não
# tiveram" em vez de "questões sequenciais". Isso elimina o
# confundimento B2; o efeito aleatório de questão no modelo estatístico
# apenas complementa esse filtro, não o substitui.
ELEGIBILIDADE_MIN_PROPORCAO_IF = 0.5

MAX_WORKERS = 3

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

# ============================================================
# ÍNDICE GLOBAL: (usuario, questao) → filepath
# Construído UMA vez no início, evita varrer disco repetidamente
# ============================================================

indice_arquivos = {}  # {(usuario_id, questao_id): filepath}

def construir_indice(pasta_usuarios):
    """
    Varre todos os usuários UMA única vez e indexa:
    (usuario_id, questao_id) → caminho do .py

    Estrutura esperada: {usuario}/codes/{prova}_{questao}.py
    O questao_id é sempre a SEGUNDA parte do nome do arquivo.
    """
    global indice_arquivos
    indice = {}
    total = 0

    for usuario_id in os.listdir(pasta_usuarios):
        codes_path = os.path.join(pasta_usuarios, usuario_id, 'codes')
        if not os.path.isdir(codes_path):
            continue
        for filename in os.listdir(codes_path):
            if not filename.endswith('.py'):
                continue
            partes = os.path.splitext(filename)[0].split('_')
            if len(partes) != 2:
                continue  # nome inesperado, ignora
            questao_id = partes[1]  # ex: '2847'
            filepath = os.path.join(codes_path, filename)
            indice[(usuario_id, questao_id)] = filepath
            total += 1

    indice_arquivos = indice
    print(f"📑 Índice construído: {total:,} arquivos indexados ({len(os.listdir(pasta_usuarios)):,} usuários)")


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
    """
    Analisa um arquivo Python e retorna uma tupla:
        (lista_de_mc3_detectados, tem_condicional)

    tem_condicional indica se ESTE código específico usa if/elif/else.
    É usado para calcular, por questão, a proporção de alunos que
    usaram condicional — base para a elegibilidade de B4/B8/B9.
    """
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            code = file.read()
        if not code or len(code.strip()) == 0:
            return [], False
        parsed = ast.parse(code)
    except Exception:
        return [], False

    visitor = VisitorMC3()
    tem_condicional = visitor.getHasConditional(parsed)

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
        detectados = [mc for mc, res in res_map.items()
                      if (res[0] if isinstance(res, tuple) else res)]
        return detectados, tem_condicional

    except Exception:
        return [], tem_condicional


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

    # Contadores para elegibilidade estrutural de B4/B8/B9
    total_analisados = 0
    total_com_condicional = 0

    atualizar_status_thread(thread_id, questao_id, "analisando_usuarios")

    for i, usuario_id in enumerate(usuarios):
        if i % 10 == 0:
            atualizar_status_thread(thread_id, questao_id, f"usuario_{i+1}/{len(usuarios)}")

        # O(1) — lookup direto no índice, sem tocar o disco
        filepath = indice_arquivos.get((str(usuario_id), questao_id_str))

        if filepath is None:
            continue  # aluno não tem arquivo para essa questão

        mc3_lista, tem_condicional = analisar_codigo(filepath)
        misconceptions = set(mc3_lista)

        total_analisados += 1
        if tem_condicional:
            total_com_condicional += 1

        detailed_results.append({
            'question': questao_id,
            'usuario': usuario_id,
            'misconceptions_detectados': ','.join(sorted(misconceptions)),
            'total_misconceptions': len(misconceptions),
            'categorias_afetadas': len(set(mc[0] for mc in misconceptions)),
            'tem_condicional': tem_condicional
        })

        for mc3 in misconceptions:
            mc3_counters[mc3] += 1

    atualizar_status_thread(thread_id, questao_id, "finalizando")

    proporcao_com_condicional = (
        total_com_condicional / total_analisados if total_analisados > 0 else 0.0
    )
    elegivel_condicional = proporcao_com_condicional >= ELEGIBILIDADE_MIN_PROPORCAO_IF

    summary_row = {
        'question': questao_id,
        'respostas': len(usuarios),
        'proporcao_com_condicional': round(proporcao_com_condicional, 4),
        # Elegibilidade estrutural para B4/B8/B9: True = a questão tem uma
        # proporção relevante de alunos usando if/elif/else, logo B4/B8/B9
        # eram estruturalmente possíveis ali. Use esta coluna para filtrar
        # o grupo de comparação de B4/B8/B9 (não filtrar os outros MC³).
        'elegivel_condicional': elegivel_condicional,
    }
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
    construir_indice(pasta_usuarios)

    if not show_progress_bar:
        print(f"\nLendo questoes_ordenadas.csv...")
    df_questoes = pd.read_csv(csv_questoes)
    total_questoes = len(df_questoes)

    if show_progress_bar:
        print(f"🎯 Iniciando análise de {total_questoes} questões com {MAX_WORKERS} threads...")
    else:
        print(f"Configuração: {MAX_WORKERS} threads para {total_questoes} questões")

    questoes_para_processar = [(row['id'], row['usuarios_respondidos'])
                                for _, row in df_questoes.iterrows()]

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

    if not show_progress_bar:
        def status_monitor():
            # Aguarda 5 segundos ou até receber o sinal de parada
            while not stop_monitor.wait(timeout=5):
                mostrar_status_threads()

        threading.Thread(target=status_monitor, daemon=True).start()

    questoes_processadas = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS, thread_name_prefix='MC3-Worker') as executor:
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