#!/usr/bin/env python3
"""
prep_notebooks_for_git.py — Limpa outputs de notebooks Jupyter e mostra
instruções de Git.

Substitui prep_notebooks_for_git.sh (que era um script Bash e só rodava
em WSL/Git Bash/Cygwin). Esta versão é Python puro e roda identicamente
em Windows (cmd/PowerShell), Linux e macOS:

    python prep_notebooks_for_git.py
"""

import glob
import json
import os
import subprocess
import sys

# Habilita interpretação de códigos ANSI de cor no cmd.exe do Windows 10+.
# Em Linux/macOS este truque não tem efeito nenhum (é ignorado).
if os.name == "nt":
    os.system("")

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def print_status(msg: str) -> None:
    print(f"{BLUE}[INFO]{NC} {msg}")


def print_success(msg: str) -> None:
    print(f"{GREEN}[SUCCESS]{NC} {msg}")


def print_warning(msg: str) -> None:
    print(f"{YELLOW}[WARNING]{NC} {msg}")


def print_error(msg: str) -> None:
    print(f"{RED}[ERROR]{NC} {msg}")


def clear_notebook_output(notebook_path: str) -> dict | None:
    try:
        size_before_mb = os.path.getsize(notebook_path) / (1024 * 1024)
        print(f"📝 Processando: {notebook_path} ({size_before_mb:.2f} MB)")

        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        cells_with_outputs = 0
        total_outputs = 0

        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                if cell.get("outputs") or cell.get("execution_count"):
                    cells_with_outputs += 1
                    total_outputs += len(cell.get("outputs", []))
                cell["outputs"] = []
                cell["execution_count"] = None
                if "metadata" in cell:
                    cell["metadata"] = {}

        if "metadata" in notebook:
            essential_keys = ["kernelspec", "language_info"]
            notebook["metadata"] = {
                k: notebook["metadata"][k]
                for k in essential_keys
                if k in notebook["metadata"]
            }

        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(notebook, f, separators=(",", ":"), ensure_ascii=False)

        size_after_mb = os.path.getsize(notebook_path) / (1024 * 1024)
        reduction_mb = size_before_mb - size_after_mb
        reduction_percent = (
            (reduction_mb / size_before_mb * 100) if size_before_mb > 0 else 0
        )

        if reduction_mb > 1:
            status = "🎉 MUITO ESPAÇO ECONOMIZADO"
        elif reduction_mb > 0.1:
            status = "✅ BOM"
        elif cells_with_outputs > 0:
            status = "🧹 LIMPO"
        else:
            status = "ℹ️  JÁ ESTAVA LIMPO"

        print(
            f"   {status}: {size_before_mb:.2f} → {size_after_mb:.2f} MB "
            f"(-{reduction_mb:.2f} MB, -{reduction_percent:.1f}%)"
        )
        print(
            f"   📊 {cells_with_outputs} células com outputs, "
            f"{total_outputs} outputs removidos"
        )

        return {
            "size_before": size_before_mb,
            "size_after": size_after_mb,
            "reduction": reduction_mb,
            "cells_cleaned": cells_with_outputs,
            "outputs_removed": total_outputs,
        }
    except Exception as e:
        print(f"❌ Erro ao limpar {notebook_path}: {e}", file=sys.stderr)
        return None


def clean_all_notebooks() -> None:
    notebooks = glob.glob("**/*.ipynb", recursive=True)

    if not notebooks:
        print("ℹ️  Nenhum notebook Jupyter encontrado no diretório atual.")
        return

    print(f"📁 Encontrados {len(notebooks)} notebook(s) para processar:")
    for nb in notebooks:
        print(f"   - {nb}")

    print("\n🔄 Analisando e limpando notebooks...\n")

    processed_count = 0
    large_files = []
    total_space_saved = 0.0
    total_outputs_removed = 0
    total_cells_cleaned = 0

    for notebook in notebooks:
        result = clear_notebook_output(notebook)
        if result is not None:
            processed_count += 1
            total_space_saved += result["reduction"]
            total_outputs_removed += result["outputs_removed"]
            total_cells_cleaned += result["cells_cleaned"]
            if result["size_after"] > 90:
                large_files.append((notebook, result["size_after"]))
        print()

    print("=" * 60)
    print("📊 RESUMO FINAL:")
    print(f"   • Notebooks processados: {processed_count}/{len(notebooks)}")
    print(f"   • Espaço total economizado: {total_space_saved:.2f} MB")
    print(f"   • Células com outputs limpas: {total_cells_cleaned}")
    print(f"   • Total de outputs removidos: {total_outputs_removed}")

    if total_space_saved > 10:
        print("   🎉 EXCELENTE! Mais de 10MB economizados!")
    elif total_space_saved > 1:
        print("   ✅ ÓTIMO! Mais de 1MB economizado!")
    elif total_space_saved > 0.1:
        print("   👍 BOM! Espaço economizado significativo!")
    else:
        print("   ℹ️  Notebooks já estavam relativamente limpos!")

    if large_files:
        print("\n⚠️  ARQUIVOS AINDA GRANDES (podem causar problemas no Git):")
        for file, size in large_files:
            print(f"   📁 {file}: {size:.2f} MB")
        print(
            "\n💡 Dica: Arquivos muito grandes podem ser rejeitados pelo "
            "GitHub (limite ~100MB)"
        )
    else:
        print("\n✅ Todos os notebooks estão com tamanho adequado para o Git!")

    print("=" * 60)


def run_git(args: list) -> subprocess.CompletedProcess | None:
    """Roda um comando git, retornando None se git não estiver disponível."""
    try:
        return subprocess.run(
            ["git", *args], capture_output=True, text=True, check=False
        )
    except FileNotFoundError:
        return None


def print_git_instructions() -> None:
    print()
    print_status("=" * 48)
    print_status("               INSTRUÇÕES GIT")
    print_status("=" * 48)

    print_status("1. 📋 Verificar o que foi alterado:")
    print("   git status")

    print_status("2. ➕ Adicionar mudanças ao stage:")
    print("   git add .")
    print("   (Para arquivos específicos: git add <caminho/do/arquivo>)")

    print_status("3. 💾 Fazer commit das mudanças:")
    print('   git commit -m "Limpar outputs dos notebooks Jupyter"')
    print("   (Personalize a mensagem conforme necessário)")

    print_status("4. 🚀 Enviar para o repositório remoto:")
    print("   git push origin main")
    print("   (Substitua 'main' pelo nome da sua branch se diferente)")

    print()
    print_status("=" * 48)
    print_status("          REPOSITÓRIOS CONECTADOS")
    print_status("=" * 48)

    if not os.path.isdir(".git"):
        print_warning("❌ Este diretório não é um repositório Git.")
        print_status("💡 Para inicializar: git init")
        return

    remotes = run_git(["remote", "-v"])
    if remotes is None:
        print_warning("Git não encontrado no PATH.")
    elif remotes.stdout.strip():
        print(remotes.stdout.strip())
    else:
        print_warning("Nenhum repositório remoto configurado.")

    branch = run_git(["branch", "--show-current"])
    current_branch = (
        branch.stdout.strip() if branch and branch.stdout.strip() else "desconhecida"
    )
    print_status(f"🌿 Branch atual: {current_branch}")

    status = run_git(["status", "--porcelain"])
    if status:
        print()
        print_status("📊 Status atual do Git:")
        lines = status.stdout.splitlines()
        for line in lines[:10]:
            print(line)
        if len(lines) > 10:
            print("   ... e mais arquivos modificados")


def main() -> None:
    print_status("🚀 Iniciando limpeza de notebooks Jupyter...")
    try:
        clean_all_notebooks()
    except Exception:
        print_error("Erro durante a limpeza dos notebooks")
        raise

    print_success("Notebooks limpos com sucesso!")
    print_git_instructions()

    print()
    print_status("=" * 48)
    print_success("✅ Script concluído com sucesso!")
    print_status("=" * 48)


if __name__ == "__main__":
    main()
