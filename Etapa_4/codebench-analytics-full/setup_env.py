# Makefile que verifica e instala o Poetry se necessário.

PROJECT_PATH=codebench_analytics/
PYTHON_EXEC := $(shell which python3)

# Opções para as ferramentas de linting e formatação
BLACK_OPTIONS := --check
RUFF_OPTIONS :=

# --- ALVOS PRINCIPAIS ---

.PHONY: all
all: setup lint

.PHONY: setup
setup: check-poetry
	@echo "🐍 Configurando ambiente Poetry para usar $(PYTHON_EXEC)..."
	@poetry env use $(PYTHON_EXEC)
	@echo "📦 Instalando dependências do projeto..."
	@poetry install
	@echo "✅ Ambiente pronto!"

.PHONY: lint
lint:
	@echo "✨ Verificando formatação e qualidade do código..."
	@poetry run black $(BLACK_OPTIONS) $(PROJECT_PATH)
	@# A linha abaixo foi modificada para ignorar o erro E501 (linha muito longa).
	@poetry run ruff check $(PROJECT_PATH) $(RUFF_OPTIONS) --ignore E501

.PHONY: format
format: RUFF_OPTIONS := --fix
format: BLACK_OPTIONS :=
format: lint

# --- ALVO DE VERIFICAÇÃO INTERNO ---

.PHONY: check-poetry
check-poetry:
	@# Verifica se o comando 'poetry' está disponível no PATH.
	@if ! command -v poetry &> /dev/null; then \
		echo "⚠️  Poetry não encontrado. Tentando instalar via apt..."; \
		sudo apt-get update && sudo apt-get install -y python3-poetry; \
		echo "✅ Poetry instalado com sucesso."; \
	else \
		echo "👍 Poetry já está instalado."; \
	fi
