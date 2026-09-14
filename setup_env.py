#!/usr/bin/env python3
"""
setup_env.py — Bootstrap do ambiente virtual do QuestionInsight.

Substitui a lógica do Makefile por um script Python puro, que roda
identicamente em Windows, Linux e macOS (sem depender de `make`,
`which` ou da estrutura de pastas `.venv/bin/...` específica do Unix).

Uso:
    python setup_env.py install   (padrão, também roda sem argumento nenhum)
    python setup_env.py clean
    python setup_env.py help
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

VENV_DIR = Path(".venv")
REQUIREMENTS = Path("requirements.txt")
IS_WINDOWS = os.name == "nt"

# Sub-projetos com seu próprio pyproject.toml que precisam ser instalados
# (em modo editável) dentro do MESMO venv da raiz, para não depender de
# uma instalação separada do Poetry (nem de `make`, que não existe nativamente
# no Windows).
SUBPROJECTS = [
    Path("Etapa_4") / "codebench-analytics-full",
]


def venv_python() -> Path:
    """Caminho do interpretador Python dentro do venv, correto por SO."""
    if IS_WINDOWS:
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def venv_pip() -> Path:
    """Caminho do pip dentro do venv, correto por SO."""
    if IS_WINDOWS:
        return VENV_DIR / "Scripts" / "pip.exe"
    return VENV_DIR / "bin" / "pip"


def activate_hint() -> str:
    """Comando de ativação do venv, correto por SO/shell."""
    if IS_WINDOWS:
        return (
            f"   {VENV_DIR}\\Scripts\\activate.bat   (cmd.exe)\n"
            f"   {VENV_DIR}\\Scripts\\Activate.ps1    (PowerShell)"
        )
    return f"   source {VENV_DIR}/bin/activate"


def run(cmd: list) -> None:
    print(f"   -> {' '.join(str(c) for c in cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"❌ Erro ao executar: {' '.join(str(c) for c in cmd)}")
        sys.exit(1)


def setup() -> None:
    print("🐍 Verificando o Python do sistema...")
    print(f"   -> Usando: {sys.executable}")

    if not VENV_DIR.exists():
        print(f"🐍 Criando ambiente virtual em '{VENV_DIR}'...")
        # sys.executable garante o Python correto em qualquer SO,
        # sem depender de 'python3' estar no PATH (Windows normalmente
        # só registra 'python' ou 'py').
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
        print("✅ Ambiente virtual criado com sucesso.")
    else:
        print(f"✅ Ambiente virtual '{VENV_DIR}' já existe.")


def install() -> None:
    setup()

    if not REQUIREMENTS.exists():
        print(f"❌ Erro: '{REQUIREMENTS}' não encontrado no diretório atual.")
        sys.exit(1)

    print("📦 Instalando/atualizando dependências do requirements.txt...")
    run([str(venv_pip()), "install", "-U", "-r", str(REQUIREMENTS)])
    print("✅ Dependências instaladas.")

    for sub in SUBPROJECTS:
        if not sub.exists():
            print(f"⚠️  Sub-projeto '{sub}' não encontrado, pulando.")
            continue
        print(f"📦 Instalando sub-projeto '{sub}' no mesmo ambiente virtual...")
        # pip lê o pyproject.toml (build-backend = poetry-core) e instala o
        # pacote e suas dependências direto no venv da raiz — não precisa
        # ter o Poetry instalado separadamente para isso.
        run([str(venv_pip()), "install", "-e", str(sub)])
    print("✅ Sub-projetos instalados.")

    print()
    print("--- Ambiente Pronto! ---")
    print()
    print(f"O ambiente virtual '{VENV_DIR}' foi criado e configurado.")
    print()
    print("👉 Para ATIVAR o ambiente, execute:")
    print(activate_hint())
    print()
    print("👉 Para DESATIVAR o ambiente quando terminar, digite:")
    print("   deactivate")


def clean() -> None:
    print("🧹 Limpando o projeto...")
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)
        print(f"   Removido: {VENV_DIR}")

    removed = 0
    for pycache in Path(".").rglob("__pycache__"):
        shutil.rmtree(pycache, ignore_errors=True)
        removed += 1
    print(f"   {removed} pasta(s) __pycache__ removida(s).")
    print("🗑️  Ambiente virtual e arquivos de cache removidos.")


def help_() -> None:
    print("Bootstrap de ambiente do QuestionInsight (cross-platform)")
    print()
    print("Comandos disponíveis:")
    print("  python setup_env.py install  -> (Padrão) Cria o venv, instala dependências e mostra como ativá-lo.")
    print("  python setup_env.py clean    -> Remove o ambiente virtual e os arquivos de cache.")
    print("  python setup_env.py help     -> Mostra esta mensagem.")


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else "install"
    commands = {"install": install, "clean": clean, "help": help_, "setup": setup}

    action = commands.get(command)
    if action is None:
        print(f"❌ Comando desconhecido: '{command}'")
        help_()
        sys.exit(1)

    action()


if __name__ == "__main__":
    main()
