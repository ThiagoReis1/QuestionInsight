# Makefile para automação de ambiente Python

# --- Configuração ---

# Nome do diretório do ambiente virtual. Padrão é .venv.
VENV_DIR := .venv

# Encontra o executável 'python3' no PATH do sistema.
# Usar 'python3' é a prática recomendada para evitar ambiguidades com o legado 'python' (Python 2).
PYTHON_SYSTEM := $(shell which python3)

# Caminhos para os executáveis DENTRO do ambiente virtual.
# Esta é a forma correta de garantir que estamos usando as ferramentas do venv.
PYTHON_VENV := $(VENV_DIR)/bin/python
PIP_VENV := $(VENV_DIR)/bin/pip

# --- Alvos (Targets) ---

# O .PHONY declara alvos que não são arquivos.
.PHONY: all setup install run clean help

# O alvo padrão, executado quando você digita apenas 'make'.
all: install

# Alvo 'setup': Cria o ambiente virtual se ele ainda não existir.
# O alvo só é executado se o arquivo 'bin/activate' não for encontrado dentro do VENV_DIR.
$(VENV_DIR)/bin/activate:
	@echo "🐍 Verificando o Python do sistema..."
	@if [ -z "$(PYTHON_SYSTEM)" ]; then \
		echo "❌ Erro: O comando 'python3' não foi encontrado no seu sistema."; \
		echo "   Por favor, instale o Python 3."; \
		exit 1; \
	fi
	@echo "   -> Usando: $(PYTHON_SYSTEM)"
	@echo "🐍 Criando ambiente virtual em '$(VENV_DIR)'..."
	$(PYTHON_SYSTEM) -m venv $(VENV_DIR)
	@echo "✅ Ambiente virtual criado com sucesso."

# Alvo 'install': Garante que o venv existe e depois instala as dependências.
# Depende do alvo de setup, então o venv será criado se necessário.
install: $(VENV_DIR)/bin/activate
	@echo "📦 Instalando dependências do requirements.txt..."
	$(PIP_VENV) install -r requirements.txt
	@echo "✅ Dependências instaladas."

# Alvo 'run': Exemplo de como executar um script principal usando o Python do venv.
# Altere 'main.py' para o nome do seu script.
run: install
	@echo "🚀 Executando o script principal..."
	$(PYTHON_VENV) main.py

# Alvo 'clean': Remove o ambiente virtual e arquivos de cache do Python.
clean:
	@echo "🧹 Limpando o projeto..."
	rm -rf $(VENV_DIR)
	rm -rf `find . -name __pycache__`
	@echo "🗑️  Ambiente virtual e arquivos de cache removidos."

# Alvo 'help': Mostra os comandos disponíveis.
help:
	@echo "Makefile para Gerenciamento de Projeto Python"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install  -> Cria o ambiente virtual e instala as dependências (padrão)."
	@echo "  make run      -> Executa o script 'main.py' com o ambiente ativado."
	@echo "  make clean    -> Remove o ambiente virtual e os arquivos de cache."
	@echo "  make help     -> Mostra esta mensagem de ajuda."

