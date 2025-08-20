#!/bin/bash

# Script para limpar outputs de notebooks Jupyter e fornecer instruções Git
# Autor: Manus
# Data: $(date +%Y-%m-%d)

set -e  # Para o script se houver algum erro

# Cores para output (CORRIGIDAS - removidas as barras extras)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se Python 3 está disponível
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 não está instalado ou não está no PATH"
    exit 1
fi

print_status "🚀 Iniciando limpeza de notebooks Jupyter..."

# Criar script Python em arquivo temporário para melhor legibilidade
cat > /tmp/clean_notebooks.py << 'EOF'
import json
import glob
import os
import sys

def clear_notebook_output(notebook_path):
    try:
        # Verificar tamanho ANTES da limpeza
        size_before_mb = os.path.getsize(notebook_path) / (1024 * 1024)
        
        print(f'📝 Processando: {notebook_path} ({size_before_mb:.2f} MB)')
        
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Contar células e outputs antes
        total_cells = len(notebook.get('cells', []))
        cells_with_outputs = 0
        total_outputs = 0
        
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                if cell.get('outputs') or cell.get('execution_count'):
                    cells_with_outputs += 1
                    total_outputs += len(cell.get('outputs', []))
                cell['outputs'] = []
                cell['execution_count'] = None
                # Limpar metadata que pode ter dados grandes
                if 'metadata' in cell:
                    cell['metadata'] = {}
        
        # Limpar metadata do notebook inteiro
        if 'metadata' in notebook:
            # Manter apenas informações essenciais
            essential_keys = ['kernelspec', 'language_info']
            new_metadata = {}
            for key in essential_keys:
                if key in notebook['metadata']:
                    new_metadata[key] = notebook['metadata'][key]
            notebook['metadata'] = new_metadata
                
        # Salvar de forma compacta
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, separators=(',', ':'), ensure_ascii=False)
        
        # Verificar tamanho DEPOIS da limpeza
        size_after_mb = os.path.getsize(notebook_path) / (1024 * 1024)
        reduction_mb = size_before_mb - size_after_mb
        reduction_percent = (reduction_mb / size_before_mb * 100) if size_before_mb > 0 else 0
        
        # Mostrar resultado com cores baseadas na economia
        if reduction_mb > 1:  # Mais de 1MB economizado
            status = "🎉 MUITO ESPAÇO ECONOMIZADO"
        elif reduction_mb > 0.1:  # Mais de 0.1MB economizado  
            status = "✅ BOM"
        elif cells_with_outputs > 0:
            status = "🧹 LIMPO"
        else:
            status = "ℹ️  JÁ ESTAVA LIMPO"
            
        print(f'   {status}: {size_before_mb:.2f} → {size_after_mb:.2f} MB (-{reduction_mb:.2f} MB, -{reduction_percent:.1f}%)')
        print(f'   📊 {cells_with_outputs} células com outputs, {total_outputs} outputs removidos')
        
        return {
            'size_before': size_before_mb,
            'size_after': size_after_mb,
            'reduction': reduction_mb,
            'cells_cleaned': cells_with_outputs,
            'outputs_removed': total_outputs
        }
    except Exception as e:
        print(f'❌ Erro ao limpar {notebook_path}: {e}', file=sys.stderr)
        return None

# Buscar notebooks
notebooks = glob.glob('**/*.ipynb', recursive=True)
processed_count = 0
large_files = []
total_space_saved = 0
total_outputs_removed = 0
total_cells_cleaned = 0

if not notebooks:
    print("ℹ️  Nenhum notebook Jupyter encontrado no diretório atual.")
    sys.exit(0)

print(f"📁 Encontrados {len(notebooks)} notebook(s) para processar:")
for nb in notebooks:
    print(f"   - {nb}")

print(f"\n🔄 Analisando e limpando notebooks...\n")

# Processar cada notebook
for notebook in notebooks:
    result = clear_notebook_output(notebook)
    if result is not None:
        processed_count += 1
        total_space_saved += result['reduction']
        total_outputs_removed += result['outputs_removed']
        total_cells_cleaned += result['cells_cleaned']
        
        if result['size_after'] > 90:  # Avisar se ainda está muito grande
            large_files.append((notebook, result['size_after']))
    print()  # Linha em branco entre notebooks

print("=" * 60)
print(f'📊 RESUMO FINAL:')
print(f'   • Notebooks processados: {processed_count}/{len(notebooks)}')
print(f'   • Espaço total economizado: {total_space_saved:.2f} MB')
print(f'   • Células com outputs limpas: {total_cells_cleaned}')
print(f'   • Total de outputs removidos: {total_outputs_removed}')

if total_space_saved > 10:
    print(f'   🎉 EXCELENTE! Mais de 10MB economizados!')
elif total_space_saved > 1:
    print(f'   ✅ ÓTIMO! Mais de 1MB economizado!')
elif total_space_saved > 0.1:
    print(f'   👍 BOM! Espaço economizado significativo!')
else:
    print(f'   ℹ️  Notebooks já estavam relativamente limpos!')

if large_files:
    print('\n⚠️  ARQUIVOS AINDA GRANDES (podem causar problemas no Git):')
    for file, size in large_files:
        print(f'   📁 {file}: {size:.2f} MB')
    print('\n💡 Dica: Arquivos muito grandes podem ser rejeitados pelo GitHub (limite ~100MB)')
else:
    print('\n✅ Todos os notebooks estão com tamanho adequado para o Git!')

print("=" * 60)
EOF

# Executar o script Python
if python3 /tmp/clean_notebooks.py; then
    print_success "Notebooks limpos com sucesso!"
else
    print_error "Erro durante a limpeza dos notebooks"
    rm -f /tmp/clean_notebooks.py
    exit 1
fi

# Limpar arquivo temporário
rm -f /tmp/clean_notebooks.py

echo ""
print_status "================================================"
print_status "               INSTRUÇÕES GIT"
print_status "================================================"

print_status "1. 📋 Verificar o que foi alterado:"
echo "   git status"

print_status "2. ➕ Adicionar mudanças ao stage:"
echo "   git add ."
echo "   (Para arquivos específicos: git add <caminho/do/arquivo>)"

print_status "3. 💾 Fazer commit das mudanças:"
echo '   git commit -m "Limpar outputs dos notebooks Jupyter"'
echo "   (Personalize a mensagem conforme necessário)"

print_status "4. 🚀 Enviar para o repositório remoto:"
echo "   git push origin main"
echo "   (Substitua 'main' pelo nome da sua branch se diferente)"

echo ""
print_status "================================================"
print_status "          REPOSITÓRIOS CONECTADOS"
print_status "================================================"

# Verificar se estamos em um repositório Git
if [ -d ".git" ]; then
    # Listar repositórios Git conectados (remotes)
    if git remote -v > /dev/null 2>&1; then
        remotes=$(git remote -v)
        if [ -n "$remotes" ]; then
            echo "$remotes"
        else
            print_warning "Nenhum repositório remoto configurado."
        fi
    else
        print_warning "Erro ao acessar repositórios remotos."
    fi
    
    # Mostrar branch atual
    current_branch=$(git branch --show-current 2>/dev/null || echo "desconhecida")
    print_status "🌿 Branch atual: $current_branch"
    
    # Mostrar status resumido
    if command -v git &> /dev/null; then
        echo ""
        print_status "📊 Status atual do Git:"
        git status --porcelain | head -10
        if [ $(git status --porcelain | wc -l) -gt 10 ]; then
            echo "   ... e mais arquivos modificados"
        fi
    fi
else
    print_warning "❌ Este diretório não é um repositório Git."
    print_status "💡 Para inicializar: git init"
fi

echo ""
print_status "================================================"
print_success "✅ Script concluído com sucesso!"
print_status "================================================"