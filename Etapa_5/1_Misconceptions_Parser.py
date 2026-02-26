from VisitorMC3 import *
import ast
import os
import pandas as pd
import csv
from collections import defaultdict
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import queue
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

# Configuração de threads
MAX_WORKERS = 3

# Lista de todos os 22 MC³ possíveis
MC3_TYPES = [
    'A2', 'A3', 'A4', 'A5', 
    'B4', 'B6', 'B8', 'B9', 'B10', 'B11', 'B12', 
    'C1', 'C2', 'C3', 'C4', 'C8', 
    'D4', 
    'E1', 'E2', 
    'G4', 'G5', 
    'H1'
]

# Lock para operações thread-safe
output_lock = threading.Lock()
progress_lock = threading.Lock()

# Controle de progresso das threads
thread_status = {}
completed_questions = set()
status_lock = threading.Lock()

def atualizar_status_thread(thread_id, questao_id, status):
    """Atualiza o status de uma thread de forma thread-safe"""
    with status_lock:
        thread_status[thread_id] = {
            'questao_id': questao_id,
            'status': status,
            'timestamp': time.time()
        }

def marcar_questao_concluida(questao_id):
    """Marca uma questão como concluída"""
    with status_lock:
        completed_questions.add(questao_id)

def obter_status_threads():
    """Obtém o status atual de todas as threads"""
    with status_lock:
        return dict(thread_status), set(completed_questions)

def analisar_codigo(filepath):
    """Analisa um arquivo Python e retorna os MC³ detectados"""
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            code = file.read()
        
        # CORREÇÃO: Verificar se o arquivo não está vazio
        if not code or len(code.strip()) == 0:
            return []
            
        parsed = ast.parse(code)
    except Exception as e:
        # MELHORIA: Log de erros para debugging
        # print(f"Erro ao analisar {filepath}: {e}")
        return []

    visitor = VisitorMC3()
    
    try:
        # Série A (Assignments & Variables)
        resA2 = visitor.getA2(parsed)
        resA3 = visitor.getA3(parsed)
        resA4 = visitor.getA4(parsed)
        resA5 = visitor.getA5(parsed)
        
        # Série B (Boolean & Control Flow)
        resB4 = visitor.getB4(parsed)
        resB6 = visitor.getB6(parsed)
        resB8 = visitor.getB8(parsed)
        resB9 = visitor.getB9(parsed)
        resB10 = visitor.getB10(parsed)
        resB11 = visitor.getB11(parsed)
        resB12 = visitor.getB12(parsed)
        
        # Série C (Control Structures & Loops)
        resC1 = visitor.getC1(parsed)
        resC2 = visitor.getC2(parsed)
        resC3 = visitor.getC3(parsed)
        resC4 = visitor.getC4(parsed, C4_MAX_ALLOWED_RANGEITER)
        resC8 = visitor.getC8(parsed)
        
        # Série D (Data & Scope)
        resD4 = visitor.getD4(parsed)
        
        # Série E (Efficiency & Data Structures)
        resE1 = visitor.getE1(parsed)
        resE2 = visitor.getE2(parsed, E2_MAX_ALLOWED_LISTS)
        
        # Série G (Good Practices & Naming)
        resG4 = visitor.getG4(parsed, G4_MIN_VAR_CHRS, G4_MIN_FNC_CHRS, G4_MAX_ALLOWED_NONSIGNIFICANT)
        resG5 = visitor.getG5(parsed)
        
        # Série H (Statements)
        resH1 = visitor.getH1(parsed)

        # Organizar resultados - alguns retornam tuplas, outros boolean
        res_map = {
            'A2': resA2,
            'A3': resA3,
            'A4': resA4[0] if isinstance(resA4, tuple) else resA4,
            'A5': resA5[0] if isinstance(resA5, tuple) else resA5,
            'B4': resB4,
            'B6': resB6,
            'B8': resB8,
            'B9': resB9,
            'B10': resB10,
            'B11': resB11,
            'B12': resB12,
            'C1': resC1,
            'C2': resC2,
            'C3': resC3,
            'C4': resC4,
            'C8': resC8,
            'D4': resD4,
            'E1': resE1,
            'E2': resE2,
            'G4': resG4,
            'G5': resG5,
            'H1': resH1
        }
        
        # Retornar apenas os MC³ detectados (True)
        detectados = [mc3 for mc3, resultado in res_map.items() if resultado]
        return detectados
        
    except Exception as e:
        # MELHORIA: Log de erros para debugging
        # print(f"Erro ao processar {filepath}: {e}")
        return []

def encontrar_arquivos_python_usuario(usuario_pasta):
    """
    CORREÇÃO CRÍTICA: Encontra todos os arquivos Python únicos do usuário
    evitando duplicatas e garantindo que cada arquivo seja contado apenas uma vez
    """
    py_files = set()  # CORREÇÃO: Usar set para evitar duplicatas
    
    try:
        # Procurar apenas no diretório raiz do usuário
        for item in os.listdir(usuario_pasta):
            item_path = os.path.join(usuario_pasta, item)
            
            if os.path.isfile(item_path) and item.endswith('.py'):
                py_files.add(item_path)
            elif os.path.isdir(item_path):
                # Procurar em subpastas (apenas 1 nível)
                try:
                    for subitem in os.listdir(item_path):
                        subitem_path = os.path.join(item_path, subitem)
                        if os.path.isfile(subitem_path) and subitem.endswith('.py'):
                            py_files.add(subitem_path)
                except PermissionError:
                    pass
    except PermissionError:
        pass
    
    return list(py_files)

def analisar_usuario_questao(usuario_id, usuario_pasta, questao_id):
    """
    CORREÇÃO CRÍTICA: Analisa um usuário específico para uma questão
    Garante que cada misconception é contado apenas UMA VEZ por usuário
    """
    # Encontrar arquivos Python do usuário
    py_files = encontrar_arquivos_python_usuario(usuario_pasta)
    
    if not py_files:
        return None, set()
    
    # CORREÇÃO: Usar set para garantir que cada MC³ é contado apenas UMA vez
    usuario_misconceptions = set()
    
    # Analisar cada arquivo e agregar misconceptions
    for py_file in py_files:
        misconceptions = analisar_codigo(py_file)
        usuario_misconceptions.update(misconceptions)
    
    # Criar resultado detalhado
    detailed_result = {
        'question': questao_id,
        'usuario': usuario_id,
        'misconceptions_detectados': ','.join(sorted(usuario_misconceptions)),
        'total_misconceptions': len(usuario_misconceptions),
        'categorias_afetadas': len(set(mc3[0] for mc3 in usuario_misconceptions))
    }
    
    return detailed_result, usuario_misconceptions

def processar_questao(questao_data):
    """Processa uma única questão e retorna os resultados"""
    questao_id, usuarios_str = questao_data
    thread_id = threading.current_thread().name
    
    # Atualizar status da thread
    atualizar_status_thread(thread_id, questao_id, "iniciando")
    
    # Converter string de usuários para lista
    usuarios = [u.strip() for u in usuarios_str.split(',')]
    
    # CORREÇÃO: Contadores mais precisos
    mc3_counters = defaultdict(int)
    usuarios_analisados = 0
    usuarios_com_misconceptions = 0
    detailed_results = []
    
    atualizar_status_thread(thread_id, questao_id, "analisando_usuarios")
    
    # Analisar cada usuário desta questão
    for i, usuario_id in enumerate(usuarios):
        # Atualizar progresso
        if i % 10 == 0:
            atualizar_status_thread(thread_id, questao_id, f"usuario_{i+1}/{len(usuarios)}")
        
        # Procurar pasta do usuário
        usuario_pasta = os.path.join(pasta_usuarios, str(usuario_id))
        
        if not os.path.exists(usuario_pasta):
            continue
        
        # CORREÇÃO: Nova função que evita duplicatas
        detailed_result, usuario_misconceptions = analisar_usuario_questao(
            usuario_id, usuario_pasta, questao_id
        )
        
        if detailed_result is None:
            continue
        
        usuarios_analisados += 1
        
        # CORREÇÃO CRÍTICA: Contar cada MC³ apenas UMA VEZ por usuário
        if len(usuario_misconceptions) > 0:
            usuarios_com_misconceptions += 1
            
            # Incrementar contador para cada misconception ÚNICO do usuário
            for mc3 in usuario_misconceptions:
                mc3_counters[mc3] += 1  # Cada MC³ conta apenas 1x por usuário
            
            detailed_results.append(detailed_result)
        else:
            # Usuário sem misconceptions
            detailed_results.append(detailed_result)
    
    atualizar_status_thread(thread_id, questao_id, "finalizando")
    
    # Criar linha do resumo para esta questão
    summary_row = {
        'question': questao_id,
        'respostas': len(usuarios)
    }
    
    # Adicionar contadores de cada MC³
    for mc3_type in MC3_TYPES:
        summary_row[mc3_type] = mc3_counters[mc3_type]
    
    # Marcar questão como concluída
    marcar_questao_concluida(questao_id)
    atualizar_status_thread(thread_id, questao_id, "concluida")
    
    return summary_row, detailed_results, mc3_counters

def gerar_relatorio_misconceptions():
    """Gera um relatório detalhado sobre os tipos de misconceptions"""
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
    """Salva os resultados de forma thread-safe"""
    with output_lock:
        print(f"\n💾 Salvando resultados...")
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_csv(output_summary, index=False, encoding='utf-8')
        
        df_detailed = pd.DataFrame(detailed_data)
        df_detailed.to_csv(output_detailed, index=False, encoding='utf-8')
        print(f"✅ Arquivos salvos: {output_summary}, {output_detailed}")

def mostrar_status_threads(show_progress_bar=False):
    """Mostra o status atual das threads"""
    current_status, completed = obter_status_threads()
    
    if not show_progress_bar:
        print("\n" + "="*60)
        print("📊 STATUS DAS THREADS")
        print("="*60)
        
        for thread_id, info in current_status.items():
            questao_id = info['questao_id']
            status = info['status']
            timestamp = time.strftime('%H:%M:%S', time.localtime(info['timestamp']))
            
            status_emoji = {
                'iniciando': '🚀',
                'analisando_usuarios': '🔍',
                'finalizando': '🔧',
                'concluida': '✅'
            }.get(status.split('_')[0], '⚙️')
            
            print(f"{status_emoji} {thread_id}: Questão {questao_id} - {status} ({timestamp})")
        
        if completed:
            print(f"\n✅ Questões concluídas ({len(completed)}): {sorted(list(completed))}")
        
        print("="*60)

def main():
    inicio_tempo = time.time()
    
    # Verificar parâmetros da linha de comando
    show_progress_bar = len(sys.argv) > 1 and sys.argv[1] == 'progressBar'
    
    # Gerar relatório de misconceptions apenas se não usar progress bar
    if not show_progress_bar:
        gerar_relatorio_misconceptions()
    
    # Ler o CSV de questões
    if not show_progress_bar:
        print(f"\nLendo questoes_ordenadas.csv...")
    df_questoes = pd.read_csv(csv_questoes)
    
    total_questoes = len(df_questoes)
    
    if show_progress_bar:
        print(f"🎯 Iniciando análise de {total_questoes} questões com {MAX_WORKERS} threads...")
    else:
        print(f"Configuração: {MAX_WORKERS} threads para {total_questoes} questões")
    
    # Preparar dados para processamento paralelo
    questoes_para_processar = [(row['id'], row['usuarios_respondidos']) for _, row in df_questoes.iterrows()]
    
    # Estruturas para armazenar os resultados
    summary_data = []
    detailed_data = []
    global_mc3_counts = defaultdict(int)
    
    # Inicializar progress bar se solicitada
    if show_progress_bar:
        pbar = tqdm(total=total_questoes, desc="📈 Processando questões", 
                   unit="questões", ncols=100, colour='green')
    
    # Processamento paralelo das questões
    if not show_progress_bar:
        print(f"\nIniciando processamento paralelo...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS, thread_name_prefix='MC3-Worker') as executor:
        # Submeter todas as questões para processamento
        future_to_questao = {
            executor.submit(processar_questao, questao_data): questao_data[0] 
            for questao_data in questoes_para_processar
        }
        
        # Coletar resultados conforme ficam prontos
        questoes_processadas = 0
        
        # Thread para mostrar status se não estiver usando progress bar
        if not show_progress_bar:
            def status_monitor():
                while questoes_processadas < total_questoes:
                    time.sleep(5)
                    if questoes_processadas < total_questoes:
                        mostrar_status_threads(show_progress_bar)
            
            status_thread = threading.Thread(target=status_monitor, daemon=True)
            status_thread.start()
        
        for future in as_completed(future_to_questao):
            questao_id = future_to_questao[future]
            try:
                summary_row, detailed_results, mc3_counters = future.result()
                
                # Adicionar resultados às listas principais (thread-safe)
                summary_data.append(summary_row)
                detailed_data.extend(detailed_results)
                
                # Atualizar contadores globais
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
    
    if show_progress_bar:
        pbar.close()
        
        print("\n📋 STATUS FINAL:")
        current_status, completed = obter_status_threads()
        for thread_id, info in current_status.items():
            print(f"  {thread_id}: ✅ Finalizada")
        print(f"  📊 Total processado: {len(completed)} questões")
    
    # Salvar resultados
    salvar_resultados_thread_safe(summary_data, detailed_data)
    
    # Calcular tempo de execução
    tempo_total = time.time() - inicio_tempo
    
    # Gerar relatório final
    print("\n" + "="*80)
    print("🎉 RELATÓRIO FINAL DE ANÁLISE")
    print("="*80)
    print(f"⏱️  Tempo total: {tempo_total:.2f} segundos")
    print(f"🔧 Threads: {MAX_WORKERS}")
    print(f"📊 Questões: {len(summary_data)}")
    print(f"👥 Análises: {len(detailed_data)}")
    
    # Mostrar estatísticas gerais
    if summary_data:
        total_usuarios_analisados = len(detailed_data)
        usuarios_com_misconceptions = sum(1 for row in detailed_data if row['total_misconceptions'] > 0)
        
        print(f"\n📈 ESTATÍSTICAS:")
        print(f"  👥 Usuários analisados: {total_usuarios_analisados:,}")
        print(f"  ⚠️  Com misconceptions: {usuarios_com_misconceptions:,}")
        print(f"  📊 Percentual: {round(usuarios_com_misconceptions/total_usuarios_analisados*100, 2)}%")
        print(f"  ⚡ Velocidade: {total_usuarios_analisados/tempo_total:.1f} usuários/seg")
        
        if not show_progress_bar:
            print(f"\n🏆 TOP 10 MC³:")
            top_mc3 = sorted(global_mc3_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            for i, (mc3, count) in enumerate(top_mc3, 1):
                perc = round(count/total_usuarios_analisados*100, 2)
                print(f"  {i:2d}. {mc3}: {count:,} ({perc}%)")
            
            print(f"\n📋 POR CATEGORIA:")
            for categoria in ['A', 'B', 'C', 'D', 'E', 'G', 'H']:
                categoria_total = sum(global_mc3_counts[mc3] for mc3 in MC3_TYPES if mc3.startswith(categoria))
                if categoria_total > 0:
                    categoria_perc = round(categoria_total/total_usuarios_analisados*100, 2)
                    tipos_categoria = [mc3 for mc3 in MC3_TYPES if mc3.startswith(categoria)]
                    print(f"  {categoria}: {categoria_total:,} ({categoria_perc}%) - {len(tipos_categoria)} tipos")

if __name__ == "__main__":
    main()