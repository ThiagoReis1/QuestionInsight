#!/usr/bin/env python3
"""Pipeline reprodutível: tabela analítica -> GLMM cruzado -> FDR -> LaTeX.

O ajuste é uma regressão logística com interceptos aleatórios cruzados de
estudante e questão, estimada por PQL com atualização Laplace aproximada.
Também permite reconstruir uma entrada "bruta" a partir da tabela analítica
já distribuída, útil para teste de reprodução.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import sparse, stats
from scipy.sparse.linalg import splu

PCS = ["G4", "B8", "B4", "B9"]
COND_PCS = ["B8", "B4", "B9"]
PREDS = ["testes", "alteracoes", "erros_logica", "erros_sintaxe", "tempo", "delecoes"]
RAW_TO_ANALYTIC = {
    "usuario": "student_id", "question": "question_id",
    "tempo_implementacao": "tempo", "num_eventos": "eventos",
    "num_eventos_del": "delecoes", "num_submissoes": "submissoes",
    "num_tests": "testes", "num_errors": "erros",
    "num_logic_errors": "erros_logica", "num_syntax_errors": "erros_sintaxe",
    "qtd_alteracoes_codigo": "alteracoes",
}


def reconstruct_raw(analytic: pd.DataFrame) -> pd.DataFrame:
    """Reconstrói um CSV bruto mínimo, sem inventar observações ou valores."""
    out = analytic.copy()
    # A coluna categórica é reconstruída somente com os PCs binários observados.
    out["misconceptions_detectados"] = out[PCS].apply(
        lambda row: ",".join(pc for pc in PCS if int(row[pc]) == 1), axis=1
    )
    out = out.rename(columns={v: k for k, v in RAW_TO_ANALYTIC.items() if v in out})
    # Colunas derivadas não pertencem à entrada bruta; elas serão recalculadas.
    out = out.drop(columns=[c for c in [*PCS, "elig_B8", "elig_B4", "elig_B9"] if c in out])
    return out


def build_table(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Aceita tanto a entrada bruta quanto uma tabela analítica previamente gerada.
    if "misconceptions_detectados" in df.columns:
        mc = df["misconceptions_detectados"].fillna("").map(
            lambda x: {t.strip() for t in str(x).split(",") if t.strip()}
        )
        for pc in PCS:
            df[pc] = mc.map(lambda s, pc=pc: int(pc in s))
        df = df.rename(columns=RAW_TO_ANALYTIC)
    elif not set(PCS).issubset(df.columns):
        raise ValueError("A entrada precisa conter misconceptions_detectados ou as colunas G4/B8/B4/B9.")
    missing = {"student_id", "question_id", *PREDS, *PCS} - set(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes: {sorted(missing)}")
    for pc in COND_PCS:
        df[f"elig_{pc}"] = df.groupby("question_id")[pc].transform("max").astype(int)
    return df


def zlog(s: pd.Series) -> np.ndarray:
    x = np.log1p(pd.to_numeric(s, errors="coerce").to_numpy(dtype=float))
    sd = x.std(ddof=0)
    if not np.isfinite(sd) or sd == 0:
        raise ValueError("Preditor sem variabilidade após log1p; não é possível padronizar.")
    return (x - x.mean()) / sd


def vif(d: pd.DataFrame, cols: list[str]) -> dict[str, float]:
    X = d[cols].to_numpy(float)
    out = {}
    for i, c in enumerate(cols):
        others = [j for j in range(len(cols)) if j != i]
        A = np.column_stack([np.ones(len(X)), X[:, others]])
        b, *_ = np.linalg.lstsq(A, X[:, i], rcond=None)
        den = np.sum((X[:, i] - X[:, i].mean()) ** 2)
        r2 = 1 - np.sum((X[:, i] - A @ b) ** 2) / den
        out[c] = 1 / (1 - r2) if r2 < 1 else np.inf
    return out


def _design_random(ids):
    _, inv = np.unique(ids, return_inverse=True)
    n, k = len(ids), int(inv.max()) + 1
    return sparse.csr_matrix((np.ones(n), (np.arange(n), inv)), shape=(n, k)), k


def fit_glmm_logit(y, X, student_ids, question_ids, max_iter=400, tol=1e-5):
    y, X = np.asarray(y, float), np.asarray(X, float)
    n, p = X.shape
    Zs, ks = _design_random(student_ids)
    Zq, kq = _design_random(question_ids)
    Z = sparse.hstack([Zs, Zq]).tocsc()
    beta, u, s2s, s2q = np.zeros(p), np.zeros(ks + kq), 1.0, 1.0
    Xs = sparse.csc_matrix(X)
    for it in range(max_iter):
        eta = np.clip(X @ beta + Z @ u, -30, 30)
        mu = 1 / (1 + np.exp(-eta)); w = np.maximum(mu * (1 - mu), 1e-9)
        z = eta + (y - mu) / w; W = sparse.diags(w)
        G_inv = sparse.diags(np.r_[np.full(ks, 1/s2s), np.full(kq, 1/s2q)])
        XtW, ZtW = Xs.T @ W, Z.T @ W
        A11 = (XtW @ Xs).toarray(); A12 = (XtW @ Z).toarray()
        A22 = (ZtW @ Z + G_inv).tocsc(); b1, b2 = XtW @ z, ZtW @ z
        lu = splu(A22); A21 = A12.T
        inv_A22_A21 = np.column_stack([lu.solve(A21[:, j]) for j in range(p)])
        inv_A22_b2 = lu.solve(b2)
        S = A11 - A12 @ inv_A22_A21
        beta_new = np.linalg.solve(S, b1 - A12 @ inv_A22_b2)
        u_new = inv_A22_b2 - inv_A22_A21 @ beta_new
        us, uq = u_new[:ks], u_new[ks:]
        wsum_s = np.asarray(Zs.T @ w).ravel(); wsum_q = np.asarray(Zq.T @ w).ravel()
        s2s_new = (np.sum(us**2) + np.sum(1/(wsum_s + 1/s2s))) / ks
        s2q_new = (np.sum(uq**2) + np.sum(1/(wsum_q + 1/s2q))) / kq
        db = np.max(np.abs(beta_new - beta)); dv = max(abs(s2s_new-s2s), abs(s2q_new-s2q))
        beta, u, s2s, s2q = beta_new, u_new, s2s_new, s2q_new
        if db < tol and dv < tol: break
    cov_beta = np.linalg.inv(S)
    return {"beta": beta, "se": np.sqrt(np.diag(cov_beta)), "s2_student": s2s,
            "s2_question": s2q, "iters": it + 1}


def fit_one(df: pd.DataFrame, pc: str) -> list[dict]:
    d = df[df[f"elig_{pc}"] == 1].copy() if pc in COND_PCS else df.copy()
    d = d.dropna(subset=PREDS).copy()
    for c in PREDS: d["z_" + c] = zlog(d[c])
    zc = ["z_" + c for c in PREDS]; v = vif(d, zc); y = d[pc].to_numpy()
    X = np.column_stack([np.ones(len(d))] + [d[c].to_numpy() for c in zc])
    r = fit_glmm_logit(y, X, d.student_id.to_numpy(), d.question_id.to_numpy())
    # R² de Nakagawa–Schielzeth em escala latente para o modelo logístico.
    var_fixed = float(np.var(X @ r["beta"], ddof=1))
    var_random = float(r["s2_student"] + r["s2_question"])
    var_residual = float(np.pi**2 / 3)
    var_total = var_fixed + var_random + var_residual
    r2_marginal = var_fixed / var_total if var_total > 0 else np.nan
    r2_conditional = (var_fixed + var_random) / var_total if var_total > 0 else np.nan
    total = var_random + var_residual
    pvals = 2 * stats.norm.sf(np.abs(r["beta"] / r["se"]))
    names = ["(intercept)"] + PREDS; rows = []
    for i, term in enumerate(names):
        rows.append({"pc": pc, "term": term, "OR": np.exp(r["beta"][i]),
            "ci_lo": np.exp(r["beta"][i] - 1.96*r["se"][i]), "ci_hi": np.exp(r["beta"][i] + 1.96*r["se"][i]),
            "p": pvals[i], "beta": r["beta"][i], "se": r["se"][i], "var_student": r["s2_student"],
            "var_question": r["s2_question"], "icc_student": r["s2_student"]/total,
            "icc_question": r["s2_question"]/total, "N": len(d), "positives": int(y.sum()),
            "prevalence": float(y.mean()), "n_students": d.student_id.nunique(),
            "n_questions": d.question_id.nunique(), "max_vif": max(v.values()),
            "var_fixed": var_fixed, "r2_marginal": r2_marginal,
            "r2_conditional": r2_conditional})
    return rows


def bh_fdr(res: pd.DataFrame) -> pd.DataFrame:
    res = res.copy(); mask = res.term != "(intercept)"; p = res.loc[mask, "p"].to_numpy()
    order = np.argsort(p); m = len(p); adj_sorted = p[order] * m / np.arange(1, m + 1)
    adj_sorted = np.minimum.accumulate(adj_sorted[::-1])[::-1]
    adj = np.empty(m); adj[order] = np.clip(adj_sorted, 0, 1)
    res.loc[mask, "p_fdr"] = adj
    return res


def write_latex(res: pd.DataFrame, out_dir: Path) -> None:
    v = res.drop_duplicates("pc").set_index("pc")
    lines = [r"\begin{table}[H]", r"\centering\footnotesize", r"\caption{Componentes de variância dos modelos logísticos de efeitos aleatórios cruzados.}", r"\label{tab:glmm_variancia}", r"\begin{tabular}{l rrrrrrr}", r"\toprule", r"PC$^3$ & $N$ & Pos. (\%) & Quest. & $\sigma^2_{est}$ & $\sigma^2_{quest}$ & ICC$_{est}$ & ICC$_{quest}$ \\", r"\midrule"]
    for pc in PCS: lines.append(f"{pc} & {int(v.loc[pc,'N']):,} & {100*v.loc[pc,'prevalence']:.1f} & {int(v.loc[pc,'n_questions'])} & {v.loc[pc,'var_student']:.3f} & {v.loc[pc,'var_question']:.3f} & {v.loc[pc,'icc_student']:.3f} & {v.loc[pc,'icc_question']:.3f} " + chr(92) * 2)
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]; (out_dir / "tab_variancia.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    labels = {"testes":"Testes", "alteracoes":"Alteracoes de codigo", "erros_logica":"Erros de logica", "erros_sintaxe":"Erros de sintaxe", "tempo":"Tempo de implementacao", "delecoes":"Eventos de delecao"}
    lines = [r"\begin{table}[H]", r"\centering\footnotesize", r"\caption{Razões de chances (OR), por desvio-padrão, com p ajustado por Benjamini--Hochberg.}", r"\label{tab:glmm_efeitos}", r"\begin{tabular}{l cccc}", r"\toprule", r"Preditor & G4 & B8 & B4 & B9 \\", r"\midrule"]
    for term in PREDS:
        cells=[]
        for pc in PCS:
            row=res[(res.pc==pc)&(res.term==term)].iloc[0]; q=row.p_fdr; stars="" if pd.isna(q) else (r"$^{***}$" if q<.001 else r"$^{**}$" if q<.01 else r"$^{*}$" if q<.05 else "")
            cells.append(f"{row.OR:.2f}{stars}")
        lines.append(labels[term] + " & " + " & ".join(cells) + " " + chr(92) * 2)
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]; (out_dir / "tab_efeitos.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_r2_latex(res: pd.DataFrame, out_dir: Path) -> None:
    v = res.drop_duplicates("pc").set_index("pc")
    lines = [r"\begin{table}[H]", r"\centering\footnotesize", r"\caption{R$^2$ marginal e condicional dos modelos GLMM em escala latente.}", r"\label{tab:glmm_r2}", r"\begin{tabular}{l rrr}", r"\toprule", "PC$^3$ & $R^2$ marginal & $R^2$ condicional & Var. fixa " + chr(92) * 2, r"\midrule"]
    for pc in PCS:
        row = v.loc[pc]
        lines.append(f"{pc} & {row['r2_marginal']:.3f} & {row['r2_conditional']:.3f} & {row['var_fixed']:.3f} " + chr(92) * 2)
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    (out_dir / "tab_ajuste.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("input_csv", type=Path); ap.add_argument("--out-dir", type=Path, default=Path(".")); ap.add_argument("--reconstruct-raw", type=Path, help="salva uma entrada bruta reconstruída antes do ajuste")
    args = ap.parse_args(argv); args.out_dir.mkdir(parents=True, exist_ok=True)
    source = pd.read_csv(args.input_csv)
    if args.reconstruct_raw:
        reconstruct_raw(source).to_csv(args.reconstruct_raw, index=False); input_path = args.reconstruct_raw
    else: input_path = args.input_csv
    analytic = build_table(input_path); analytic.to_csv(args.out_dir / "tabela_analitica.csv", index=False)
    result = bh_fdr(pd.DataFrame(sum((fit_one(analytic, pc) for pc in PCS), [])))
    result.to_csv(args.out_dir / "glmm_final.csv", index=False); write_latex(result, args.out_dir); write_r2_latex(result, args.out_dir)
    result.drop_duplicates("pc")[["pc", "var_fixed", "var_student", "var_question", "icc_student", "icc_question", "r2_marginal", "r2_conditional", "N", "positives", "prevalence", "max_vif"]].to_csv(args.out_dir / "glmm_ajuste.csv", index=False)
    print(result[result.term != "(intercept)"][['pc','term','OR','ci_lo','ci_hi','p_fdr']].to_string(index=False))


if __name__ == "__main__": main()

__all__ = ["main", "build_table", "fit_glmm_logit", "fit_one", "bh_fdr", "reconstruct_raw"]
