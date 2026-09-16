# Adapted from: https://github.com/marcosmapl/codebench-mining-tool/

import keyword
import os
import re
import tempfile
import token
import tokenize
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from collections import Counter, defaultdict
from typing import Dict, List

import numpy as np
from radon.metrics import h_visit
from radon.raw import analyze
from radon.visitors import ComplexityVisitor

import codebench_analytics.model.token_mapping as tkm
from codebench_analytics.model.code_metrics import SolutionMetrics


class Solution:
    """Extract metrics from codebench solutions logs."""

    __type_list = [
        "bool",
        "bytes",
        "bytearray",
        "complex",
        "dict",
        "float",
        "set",
        "int",
        "list",
        "range",
        "object",
        "str",
        "memoryview",
        "None",
        "frozenset",
    ]
    __builtin_types = set(__type_list)

    __f_list = [
        "abs",
        "all",
        "any",
        "ascii",
        "bin",
        "bool",
        "bytearray",
        "bytes",
        "callable",
        "chr",
        "classmethod",
        "compile",
        "delattr",
        "dir",
        "divmod",
        "enumerate",
        "eval",
        "exec",
        "filter",
        "format",
        "getattr",
        "globals",
        "hasattr",
        "hash",
        "hex",
        "id",
        "input",
        "isinstance",
        "issubclass",
        "iter",
        "len",
        "locals",
        "map",
        "max",
        "min",
        "next",
        "oct",
        "open",
        "ord",
        "pow",
        "print",
        "property",
        "range",
        "repr",
        "reversed",
        "round",
        "set",
        "setattr",
        "slice",
        "sorted",
        "staticmethod",
        "str",
        "sum",
        "super",
        "tuple",
        "type",
        "vars",
        "zip",
    ]
    __builtin_funcs = set(__f_list)

    @staticmethod
    def __is_builtin_func(name: str):
        return name in Solution.__builtin_funcs

    @staticmethod
    def __is_builtin_type(name: str):
        return name in Solution.__builtin_types

    @staticmethod
    def extract(base_src: str):
        """Extract metrics in parallel; output order remains deterministic."""
        paths = [os.path.join(base_src, name) for name in sorted(os.listdir(base_src))]
        worker_count = max(1, min(int(os.environ.get('CODEBENCH_METRICS_WORKERS', multiprocessing.cpu_count() or 1)), 8))
        if len(paths) <= 1 or worker_count == 1:
            metric_rows = [Solution._Solution__extract_solution_metrics(path) for path in paths]
        else:
            with ProcessPoolExecutor(max_workers=worker_count) as executor:
                metric_rows = list(executor.map(_extract_solution_metrics_task, paths, chunksize=8))
        data: List[SolutionMetrics] = []
        for metric_row in metric_rows:
            solution = SolutionMetrics()
            for attr, value in metric_row.items():
                setattr(solution, attr, value)
            data.append(solution)
        return data

    @staticmethod
    def extract_from_professor(csv_src: str):
        data: Dict[int, SolutionMetrics] = {}
        temporary_files = []
        try:
            with open(csv_src, "r", encoding="utf-8") as csv_file:
                text = "".join(csv_file.readlines())
            solutions = re.split(r"#!#!#", text)
            pending = []
            for sol in solutions:
                sol = sol.strip()
                if not sol:
                    continue
                match = re.match(r"^\s*(\d+)#;#;#", sol)
                if not match:
                    raise AssertionError(f"not found id for solution: {sol}")
                solution_id = int(match.group(1))
                code = sol.split("#;#;#", 1)[1]
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".py", delete=False) as tmp_writer:
                    tmp_writer.write(code)
                    tmp_code_src = tmp_writer.name
                temporary_files.append(tmp_code_src)
                pending.append((solution_id, tmp_code_src))

            worker_count = max(1, min(int(os.environ.get('CODEBENCH_METRICS_WORKERS', multiprocessing.cpu_count() or 1)), 8))
            paths = [path for _solution_id, path in pending]
            if len(paths) <= 1 or worker_count == 1:
                metric_rows = [Solution._Solution__extract_solution_metrics(path) for path in paths]
            else:
                with ProcessPoolExecutor(max_workers=worker_count) as executor:
                    metric_rows = list(executor.map(_extract_solution_metrics_task, paths, chunksize=8))
            for (solution_id, _path), metric_row in zip(pending, metric_rows):
                solution = SolutionMetrics()
                for attr, value in metric_row.items():
                    setattr(solution, attr, value)
                data[solution_id] = solution
            return data
        finally:
            for path in temporary_files:
                try:
                    os.unlink(path)
                except OSError:
                    pass

    @staticmethod
    def __extract_solution_metrics(code_file_src: str):
        metrics = dict()
        with open(code_file_src, "r", encoding="utf-8") as f:
            codigo = "".join(f.readlines())

            try:
                v = ComplexityVisitor.from_code(codigo)
                metrics["complexity"] = v.complexity
                metrics["n_functions"] = len(v.functions)
                metrics["n_classes"] = len(v.functions)
            except BaseException:
                pass

            try:
                a = analyze(codigo)
                metrics["loc"] = a.loc
                metrics["lloc"] = a.lloc
                metrics["sloc"] = a.sloc
                metrics["blank_lines"] = a.blank
                metrics["comments"] = a.comments
                metrics["single_comments"] = a.single_comments
                metrics["multi_comments"] = a.multi
            except BaseException:
                pass

            try:
                h = h_visit(codigo)
                metrics["h1"] = h.total.h1
                metrics["h2"] = h.total.h2
                metrics["N1"] = h.total.N1
                metrics["N2"] = h.total.N2
                metrics["h"] = h.total.vocabulary
                metrics["N"] = h.total.length
                metrics["calculated_N"] = h.total.calculated_length
                metrics["volume"] = h.total.volume
                metrics["difficulty"] = h.total.difficulty
                metrics["effort"] = h.total.effort
                metrics["bugs"] = h.total.bugs
                metrics["time"] = h.total.time
            except BaseException:
                pass

            try:
                token_count = defaultdict(int)
                unique_identifiers = set()
                unique_strings = set()
                unique_btype = set()
                unique_bfunc = set()
                with tokenize.open(code_file_src) as f:
                    try:
                        tokens = tokenize.generate_tokens(f.readline)
                        for tk in tokens:
                            if tk.exact_type == token.NUMBER:
                                if "." in tk.string:
                                    token_count[tkm.NUMBER_FLOAT] += 1
                                else:
                                    token_count[tkm.NUMBER_INT] += 1
                            elif tk.type == token.NAME:
                                if keyword.iskeyword(tk.string):
                                    token_count[
                                        tkm.tk_codes.get(
                                            tk.string.lower(), tkm.KEYWORD
                                        )
                                    ] += 1
                                elif Solution.__is_builtin_type(tk.string):
                                    token_count[tkm.BUILTIN_TYPE] += 1
                                    unique_btype.add(tk.string)
                                elif Solution.__is_builtin_func(tk.string):
                                    if tk.string == "print":
                                        token_count[tkm.KWD_PRINT] += 1
                                    elif tk.string == "input":
                                        token_count[tkm.KWD_INPUT] += 1
                                    else:
                                        token_count[tkm.BUILTIN_FUNC] += 1
                                    unique_bfunc.add(tk.string)
                                else:
                                    token_count[tkm.IDENTIFIER] += 1
                                    unique_identifiers.add(tk.string)
                            elif tk.type == token.STRING:
                                token_count[tkm.STRING] += 1
                                unique_strings.add(tk.string)
                            else:
                                token_count[tk.exact_type] += 1
                    except BaseException:
                        pass

                for k, v in Counter(token_count).items():
                    metrics[tkm.tk_names[k]] = v

                metrics["builtin_type_unique"] = len(unique_btype)
                metrics["builtin_func_unique"] = len(unique_bfunc)
                metrics["identifiers_unique"] = len(unique_identifiers)

                # Check for empty lists before calculating min, max, and mean
                identifiers_lengths = [len(x) for x in unique_identifiers]
                metrics["identifiers_max_len"] = max(identifiers_lengths, default=0)
                metrics["identifiers_min_len"] = min(identifiers_lengths, default=0)
                metrics["identifiers_mean_len"] = (
                    np.mean(identifiers_lengths) if identifiers_lengths else 0
                )

            except BaseException:
                pass

        return metrics


def _extract_solution_metrics_task(path: str):
    return Solution._Solution__extract_solution_metrics(path)
