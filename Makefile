# Makefile para automação de ambiente Python
# Focado em setup e instruções para o usuário (v2)

# --- Configuração ---
VENV_DIR := .venv
PYTHON_SYSTEM := $(shell which python3)
PIP_VENV := $(VENV_DIR)/bin/pip
# Define o SHELL a ser usado para garantir consistência
SHELL := /bin/bash

# --- Alvos (Targets) ---
.PHONY: all setup install clean help

# O alvo padrão, executado quando você digita apenas 'make'.
# Agora aponta para 'install'.
all: install

# Alvo 'setup': Cria o ambiente virtual.
setup: $(VENV_DIR)/bin/activate

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

# Alvo 'install': Garante que o venv existe, instala as dependências e mostra instruções.
install: setup
	@echo "📦 Instalando/atualizando dependências do requirements.txt..."
	$(PIP_VENV) install -r requirements.txt
	@echo "✅ Dependências instaladas."
	@echo ""
	@echo "--- Ambiente Pronto! ---"
	@echo ""
	@echo "O ambiente virtual '$(VENV_DIR)' foi criado e configurado."
	@echo ""
	@echo "👉 Para ATIVAR o ambiente, execute um dos seguintes comandos:"
	@echo "   source $(VENV_DIR)/bin/activate"
	@echo ""
	@echo "   ou a forma mais curta:"
	@echo "   . $(VENV_DIR)/bin/activate"
	@echo ""
	@echo "👉 Para DESATIVAR o ambiente quando terminar, digite:"
	@echo "   deactivate"
	@echo ""

# Alvo 'clean': Remove o ambiente virtual e arquivos de cache do Python.
clean:
	@echo "🧹 Limpando o projeto..."
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "🗑️  Ambiente virtual e arquivos de cache removidos."

# Alvo 'help': Mostra os comandos disponíveis.
help:
	@echo "Makefile para Gerenciamento de Projeto Python"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install  -> (Padrão) Cria o ambiente virtual, instala as dependências e mostra como ativá-lo."
	@echo "  make clean    -> Remove o ambiente virtual e os arquivos de cache."
	@echo "  make help     -> Mostra esta mensagem de ajuda."

