#!/bin/bash

# Script para sincronizar o repositório QuestionInsight com o GitHub
# Autor: Script gerado para facilitar atualizações do repositório
# Data: $(date +%Y-%m-%d)

set -e  # Para o script se houver algum erro

echo "🚀 Iniciando sincronização com o GitHub..."
echo "================================================"

# Cores para output
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

# Função para limpar histórico do Git de arquivos grandes
clean_git_history() {
    print_warning "Limpando histórico do Git para remover arquivos grandes..."
    echo "Isso removerá todo o histórico e criará um repositório limpo."
    echo "Deseja continuar? (s/N): "
    read response
    if [[ "$response" =~ ^[Ss]$ ]]; then
        # Backup da configuração atual
        CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "$REPO_URL")
        
        # Remover .git e recriar
        print_status "Removendo histórico antigo..."
        rm -rf .git
        
        print_status "Inicializando novo repositório..."
        git init
        git remote add origin "$CURRENT_REMOTE"
        
        # Adicionar arquivos limpos
        print_status "Adicionando arquivos ao novo repositório..."
        git add .
        git commit -m "Repositório limpo - histórico recriado $(date '+%Y-%m-%d %H:%M:%S')"
        git branch -M main
        
        print_success "Histórico limpo! Repositório recriado com sucesso."
        return 0
    else
        print_status "Operação cancelada"
        return 1
    fi
}

# Função para usar BFG Repo-Cleaner (alternativa mais avançada)
use_bfg_cleaner() {
    print_status "Tentando usar BFG Repo-Cleaner para remover arquivos grandes..."
    
    # Verificar se o BFG está disponível
    if command -v bfg &> /dev/null; then
        print_status "BFG encontrado. Removendo arquivos maiores que 50MB..."
        
        # Usar BFG para remover arquivos grandes
        bfg --strip-blobs-bigger-than 50M
        git reflog expire --expire=now --all && git gc --prune=now --aggressive
        
        print_success "BFG limpeza concluída!"
        return 0
    else
        print_warning "BFG Repo-Cleaner não está instalado."
        print_status "Para instalar: sudo apt-get install bfg ou baixe de https://rtyley.github.io/bfg-repo-cleaner/"
        return 1
    fi
}

# Função para remover arquivo específico do histórico usando git filter-branch
remove_large_file_from_history() {
    local file_path="$1"
    print_warning "Removendo '$file_path' do histórico do Git..."
    
    echo "Isso irá reescrever todo o histórico removendo o arquivo '$file_path'."
    echo "ATENÇÃO: Esta operação é irreversível!"
    echo "Deseja continuar? (s/N): "
    read response
    
    if [[ "$response" =~ ^[Ss]$ ]]; then
        print_status "Iniciando remoção do arquivo do histórico..."
        
        # Usar git filter-branch para remover o arquivo
        print_status "Removendo arquivo do histórico (isso pode demorar)..."
        git filter-branch --force --index-filter \
            "git rm --cached --ignore-unmatch '$file_path'" \
            --prune-empty --tag-name-filter cat -- --all
        
        # Limpar referências
        print_status "Limpando referências..."
        git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
        git reflog expire --expire=now --all
        git gc --prune=now --aggressive
        
        print_success "Arquivo '$file_path' removido do histórico!"
        return 0
    else
        print_status "Operação cancelada"
        return 1
    fi
}

# Verificar se estamos na pasta correta
if [ ! -f "README.md" ]; then
    print_error "Execute este script na pasta raiz do projeto QuestionInsight (onde está o README.md)"
    exit 1
fi

# Configurar Git se necessário
print_status "Verificando configuração do Git..."
if [ -z "$(git config --global user.name)" ]; then
    echo -n "Digite seu nome para o Git: "
    read git_name
    git config --global user.name "$git_name"
fi

if [ -z "$(git config --global user.email)" ]; then
    echo -n "Digite seu email para o Git: "
    read git_email
    git config --global user.email "$git_email"
fi

# Inicializar o repositório se ainda não foi inicializado
print_status "Inicializando repositório Git..."
if [ ! -d ".git" ]; then
    git init
    print_success "Repositório Git inicializado"
else
    print_success "Repositório Git já existe"
fi

# Configurar remote
print_status "Configurando repositório remoto..."
REPO_URL="https://github.com/ThiagoReis1/QuestionInsight.git"

if git remote get-url origin > /dev/null 2>&1; then
    git remote set-url origin "$REPO_URL"
    print_success "URL do repositório remoto atualizada"
else
    git remote add origin "$REPO_URL"
    print_success "Repositório remoto adicionado"
fi

# Remover arquivos que devem ser ignorados do controle de versão
print_status "Removendo arquivos que devem ser ignorados..."

# Arrays com pastas e arquivos para remover
folders_to_remove=(
    "CSVS_JO/"
    "Etapa_3/Processamento/"
    "Etapa_3/UsuariosUnicos/"
    "Etapa_4/codebench-analytics-full/output/"
    "Etapa_5/Provas/"
    "Etapa_5/Provas_Arrumadas/"
    "Extraidos/"
)

files_to_remove=(
    "Etapa_3/questoes_ordenadas.csv"
    "Etapa_4/code_metrics_professor_util.csv"
    "Etapa_4/assessments.csv"
    "Etapa_4/question_new_info.csv"
    "Etapa_4/resultado.csv"
    "Etapa_5/misconceptions_detailed_por_usuario.csv"
    "Etapa_5/misconceptions_summary_por_questao.csv"
    "Etapa_5/questions_D_M.csv"
)

# Remover pastas
for folder in "${folders_to_remove[@]}"; do
    if git ls-files --error-unmatch "$folder" > /dev/null 2>&1; then
        git rm -r --cached "$folder" 2>/dev/null || true
        print_success "Pasta removida do Git: $folder"
    fi
done

# Remover arquivos
for file in "${files_to_remove[@]}"; do
    if git ls-files --error-unmatch "$file" > /dev/null 2>&1; then
        git rm --cached "$file" 2>/dev/null || true
        print_success "Arquivo removido do Git: $file"
    fi
done

# Limpar outputs dos notebooks Jupyter para reduzir tamanho
print_status "Limpando outputs dos notebooks Jupyter..."

# Método mais agressivo de limpeza usando Python
python3 -c "
import json
import glob
import os

def clear_notebook_output(notebook_path):
    try:
        print(f'Processando: {notebook_path}')
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Contar células antes
        total_cells = len(notebook.get('cells', []))
        
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
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
        
        # Verificar tamanho final
        size_mb = os.path.getsize(notebook_path) / (1024 * 1024)
        print(f'✓ Limpo: {notebook_path} ({size_mb:.2f} MB)')
        return size_mb
    except Exception as e:
        print(f'Erro ao limpar {notebook_path}: {e}')
        return None

notebooks = glob.glob('**/*.ipynb', recursive=True)
cleaned = 0
large_files = []

for notebook in notebooks:
    size = clear_notebook_output(notebook)
    if size is not None:
        cleaned += 1
        if size > 90:  # Avisar se ainda está muito grande
            large_files.append((notebook, size))

print(f'\\nTotal de notebooks limpos: {cleaned}')

if large_files:
    print('\\n⚠️  ARQUIVOS AINDA GRANDES (podem causar problemas):')
    for file, size in large_files:
        print(f'   {file}: {size:.2f} MB')
" 2>/dev/null || true

print_success "Notebooks limpos de forma agressiva"

# Verificar se existe .gitignore e criar se necessário
if [ ! -f ".gitignore" ]; then
    print_warning ".gitignore não encontrado. Criando um básico..."
    cat > .gitignore << 'EOF'
# Arquivos de dados e processamento
CSVS_JO/
Etapa_3/Processamento/
Etapa_3/UsuariosUnicos/
Etapa_4/codebench-analytics-full/output/
Etapa_5/Provas/
Etapa_5/Provas_Arrumadas/
Extraidos/

# Arquivos CSV gerados
Etapa_3/questoes_ordenadas.csv
Etapa_4/code_metrics_professor_util.csv
Etapa_4/assessments.csv
Etapa_4/question_new_info.csv
Etapa_4/resultado.csv
Etapa_5/misconceptions_detailed_por_usuario.csv
Etapa_5/misconceptions_summary_por_questao.csv
Etapa_5/questions_D_M.csv

# Arquivos do sistema
.DS_Store
Thumbs.db
*.log
*.tmp
*~

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Jupyter Notebooks checkpoints
.ipynb_checkpoints/

# Arquivos grandes (Git LFS)
*.zip
*.tar.gz
*.rar
*.7z
EOF
    print_success ".gitignore criado"
fi

# Adicionar todos os arquivos (respeitando o .gitignore)
print_status "Adicionando arquivos ao Git..."
git add .
print_success "Arquivos adicionados"

# Verificar se há mudanças para commit ou se já há commits não enviados
COMMITS_AHEAD=$(git rev-list --count HEAD ^origin/main 2>/dev/null || echo "0")
HAS_STAGED_CHANGES=$(git diff --staged --quiet && echo "false" || echo "true")
HAS_UNSTAGED_CHANGES=$(git diff --quiet && echo "false" || echo "true")

if [ "$HAS_STAGED_CHANGES" = "false" ] && [ "$HAS_UNSTAGED_CHANGES" = "false" ]; then
    if [ "$COMMITS_AHEAD" -gt 0 ]; then
        print_warning "Nenhuma mudança nova detectada, mas há $COMMITS_AHEAD commit(s) local(is) não enviado(s)"
        echo "Deseja enviar os commits existentes para o GitHub? (s/N): "
        read -r response
        if [[ ! "$response" =~ ^[Ss]$ ]]; then
            print_status "Operação cancelada"
            exit 0
        fi
        # Pular a criação de novo commit
        SKIP_COMMIT=true
    else
        print_warning "Nenhuma mudança detectada para commit"
        echo "Deseja continuar mesmo assim? (s/N): "
        read -r response
        if [[ ! "$response" =~ ^[Ss]$ ]]; then
            print_status "Operação cancelada"
            exit 0
        fi
        SKIP_COMMIT=true
    fi
else
    SKIP_COMMIT=false
fi

# Fazer commit apenas se houver mudanças
if [ "$SKIP_COMMIT" = "false" ]; then
    # Pedir mensagem de commit personalizada
    echo -n "Digite uma mensagem de commit (ou pressione Enter para usar a padrão): "
    read commit_message

    if [ -z "$commit_message" ]; then
        commit_message="Atualizar repositório - $(date '+%Y-%m-%d %H:%M:%S')"
    fi

    # Fazer commit
    print_status "Fazendo commit..."
    if git commit -m "$commit_message"; then
        print_success "Commit realizado: $commit_message"
    else
        print_warning "Não foi possível fazer commit (pode ser que não há mudanças)"
    fi
else
    print_status "Pulando criação de novo commit..."
    commit_message="Commits existentes"
fi

# Configurar branch principal como main
print_status "Configurando branch principal..."
git branch -M main
print_success "Branch configurada como main"

# Verificar tamanhos dos arquivos antes de tentar push
print_status "Verificando tamanhos dos arquivos..."
large_files_found=false
large_files_in_history=()

# Verificar arquivos atuais
while IFS= read -r -d '' file; do
    size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo "0")
    size_mb=$((size / 1024 / 1024))
    
    if [ $size_mb -gt 90 ]; then
        if [ "$large_files_found" = false ]; then
            print_error "⚠️  ARQUIVOS MUITO GRANDES ENCONTRADOS:"
            large_files_found=true
        fi
        printf "   %-50s %d MB\n" "$file" "$size_mb"
    fi
done < <(git ls-files -z)

# Verificar se há versões grandes no histórico do Git
print_status "Verificando histórico do Git para arquivos grandes..."
while IFS= read -r line; do
    if [ -n "$line" ]; then
        large_files_in_history+=("$line")
    fi
done < <(git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
awk '/^blob/ {if ($3 > 90*1024*1024) print $4 " (" int($3/1024/1024) " MB)"}')

# Se encontrou arquivos grandes no histórico, oferecer soluções
if [ ${#large_files_in_history[@]} -gt 0 ]; then
    print_error "⚠️  ARQUIVOS GRANDES ENCONTRADOS NO HISTÓRICO DO GIT:"
    for file_info in "${large_files_in_history[@]}"; do
        echo "   $file_info"
    done
    echo ""
    echo "Soluções disponíveis:"
    echo "1. Limpar histórico completo (recomendado) - recria repositório sem histórico antigo"
    echo "2. Remover arquivo específico do histórico (avançado)"
    echo "3. Tentar usar BFG Repo-Cleaner (se disponível)"
    echo "4. Continuar mesmo assim (pode falhar)"
    echo "5. Cancelar"
    echo ""
    echo -n "Escolha uma opção (1/2/3/4/5): "
    read option
    
    case $option in
        1)
            if clean_git_history; then
                print_success "Histórico limpo! Continuando com push..."
            else
                exit 0
            fi
            ;;
        2)
            echo "Arquivos encontrados no histórico:"
            for i in "${!large_files_in_history[@]}"; do
                echo "$((i+1)). ${large_files_in_history[$i]}"
            done
            echo -n "Digite o nome completo do arquivo para remover (ex: Etapa_1/Etapa_1.ipynb): "
            read file_to_remove
            if [ -n "$file_to_remove" ]; then
                if remove_large_file_from_history "$file_to_remove"; then
                    print_success "Arquivo removido do histórico! Continuando com push..."
                else
                    exit 0
                fi
            else
                print_error "Nome do arquivo não fornecido. Cancelando."
                exit 1
            fi
            ;;
        3)
            if use_bfg_cleaner; then
                print_success "BFG limpeza concluída! Continuando com push..."
            else
                echo "Escolha outra opção:"
                exec "$0"  # Reinicia o script
            fi
            ;;
        4)
            print_warning "Continuando mesmo com arquivos grandes no histórico..."
            ;;
        5)
            print_status "Operação cancelada pelo usuário"
            exit 0
            ;;
        *)
            print_error "Opção inválida. Cancelando."
            exit 1
            ;;
    esac
fi

if [ "$large_files_found" = true ]; then
    print_error "GitHub tem limite de 100MB por arquivo!"
    echo "Deseja continuar mesmo assim? Pode falhar. (s/N): "
    read -r response
    if [[ ! "$response" =~ ^[Ss]$ ]]; then
        print_status "Push cancelado. Resolva os arquivos grandes primeiro."
        exit 1
    fi
elif [ ${#large_files_in_history[@]} -eq 0 ]; then
    print_success "Todos os arquivos estão dentro do limite do GitHub"
fi

# Testar credenciais do GitHub ANTES de tentar push
print_status "Testando conexão com GitHub..."
echo "Vamos testar suas credenciais do GitHub primeiro:"

# Fazer um fetch simples para forçar autenticação
if git ls-remote origin >/dev/null 2>&1; then
    print_success "Credenciais do GitHub funcionando!"
else
    print_warning "Precisamos das suas credenciais do GitHub"
    echo "Por favor, forneça suas credenciais quando solicitado:"
    
    # Forçar uma operação que requer autenticação
    git ls-remote origin || {
        print_error "Falha na autenticação com GitHub!"
        echo "Verifique suas credenciais e tente novamente."
        exit 1
    }
    print_success "Autenticação bem-sucedida!"
fi

# Verificar se há commits para enviar
COMMITS_TO_PUSH=$(git rev-list --count HEAD ^origin/main 2>/dev/null || git rev-list --count HEAD 2>/dev/null || echo "0")

if [ "$COMMITS_TO_PUSH" -eq 0 ]; then
    print_warning "Não há commits novos para enviar ao GitHub"
    echo "Deseja forçar um push mesmo assim? (s/N): "
    read -r response
    if [[ ! "$response" =~ ^[Ss]$ ]]; then
        print_status "Operação cancelada"
        echo "Repositório já está sincronizado!"
        exit 0
    fi
else
    print_status "Há $COMMITS_TO_PUSH commit(s) para enviar ao GitHub"
fi

# Push para o GitHub
print_status "Enviando para o GitHub..."

# Verificar se precisamos usar --force
if git status | grep -q "Your branch is ahead of"; then
    print_warning "Branch local está à frente do remoto"
    echo "Deseja fazer push normal (recomendado) ou forçar? (n/F): "
    read -r push_type
    if [[ "$push_type" =~ ^[Ff]$ ]]; then
        PUSH_FORCE="--force"
        print_warning "ATENÇÃO: Será feito um push com --force que pode sobrescrever o repositório remoto!"
    else
        PUSH_FORCE=""
        print_status "Fazendo push normal..."
    fi
else
    PUSH_FORCE=""
fi

echo "Deseja continuar com o push? (s/N): "
read -r response

if [[ "$response" =~ ^[Ss]$ ]]; then
    print_status "Iniciando push para o GitHub..."
    
    if git push -u origin main $PUSH_FORCE; then
        print_success "Repositório sincronizado com sucesso!"
        echo "================================================"
        echo "🎉 Sincronização concluída!"
        echo "📂 Repositório: $REPO_URL"
        echo "📝 Último commit: $commit_message"
        echo "📊 Commits enviados: $COMMITS_TO_PUSH"
        echo "🕒 Data: $(date '+%Y-%m-%d %H:%M:%S')"
    else
        print_error "Falha ao enviar para o GitHub"
        echo "Possíveis soluções:"
        echo "1. Verifique suas credenciais do GitHub"
        echo "2. Verifique sua conexão com a internet"
        echo "3. Certifique-se de ter permissão de escrita no repositório"
        echo "4. Execute o script novamente e escolha a opção 1 para limpar o histórico"
        exit 1
    fi
else
    print_status "Push cancelado pelo usuário"
    if [ "$COMMITS_TO_PUSH" -gt 0 ]; then
        echo "Os commits foram realizados localmente, mas não foram enviados para o GitHub"
    fi
fi

echo "================================================"