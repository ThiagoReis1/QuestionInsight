"""VisitorMC3: motor de análise estática do PC3 baseado na AST do Python para identificar padrões associados a misconceptions em código.

A API pública executa cada detector sem reutilizar estado entre árvores sintáticas."""

import ast
from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True)
class MC3Config:
    """Configuração dos critérios dos detectores MC³ do PC3."""
    c4_range_threshold: int = 50
    e2_list_threshold: int = 5
    g4_min_var_chars: int = 4
    g4_min_func_chars: int = 8
    g4_max_nonsignificant_percent: int = 70


@dataclass(frozen=True)
class ASTSnapshot:
    """Dados estruturais coletados em uma única travessia da árvore.

    A tupla é imutável e nunca é compartilhada como estado mutável entre
    detectores. Cada detector pode, portanto, usar o mesmo snapshot sem
    alterar a análise de outro detector.
    """
    root: ast.AST
    nodes: tuple
    by_type: dict

    @classmethod
    def collect(cls, root):
        nodes = tuple(ast.walk(root))
        by_type = {}
        for node in nodes:
            by_type.setdefault(type(node), []).append(node)
        return cls(root=root, nodes=nodes,
                   by_type=MappingProxyType({
                       kind: tuple(items) for kind, items in by_type.items()
                   }))


# =============================================================================
# CLASSE AUXILIAR
# =============================================================================

class VisitorMC3Helper:

    @staticmethod
    def compare_ast_nodes(node1, node2):
        """Componente do motor de análise estática do PC3."""
        if isinstance(node1, ast.Name) and isinstance(node2, ast.Name):
            return node1.id == node2.id
        if isinstance(node1, ast.Constant) and isinstance(node2, ast.Constant):
            return node1.value == node2.value
        if type(node1) == type(node2):
            return ast.dump(node1) == ast.dump(node2)
        return False

    @staticmethod
    def get_inverse_op(op):
        inverse_map = {
            ast.Eq: ast.NotEq, ast.NotEq: ast.Eq,
            ast.Lt: ast.GtE,   ast.LtE: ast.Gt,
            ast.Gt: ast.LtE,   ast.GtE: ast.Lt,
            ast.In: ast.NotIn, ast.NotIn: ast.In,
            ast.Is: ast.IsNot, ast.IsNot: ast.Is,
        }
        return inverse_map.get(type(op))

    @staticmethod
    def compare_ops_equal(ops1, ops2):
        if len(ops1) != len(ops2) or len(ops1) != 1:
            return False
        return type(ops1[0]) == type(ops2[0])

    @staticmethod
    def compare_ops_inverse(ops1, ops2):
        if len(ops1) != len(ops2) or len(ops1) != 1:
            return False
        return VisitorMC3Helper.get_inverse_op(ops1[0]) == type(ops2[0])

    @staticmethod
    def compare_comparators(comps1, comps2):
        if len(comps1) != len(comps2) or len(comps1) != 1:
            return False
        return VisitorMC3Helper.compare_ast_nodes(comps1[0], comps2[0])

    @staticmethod
    def is_block_comment(node):
        if isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Constant):
                if isinstance(node.value.value, str):
                    return True
        return False


# =============================================================================
# CLASSE PRINCIPAL
# =============================================================================

class VisitorMC3(ast.NodeVisitor):

    def __init__(self):
        # Categoria A
        self.builtinRedefinition = False
        self.declaredVariablesAsBuiltIn = set()
        self.declaredFunctionsAsBuiltin = set()
        self.declaredArgumentsAsBuiltin = set()
        self.selfAssignment = False
        self.unusedInitVar = False
        self.unusedImports = []
        # Categoria B
        self.boolOpAttemptedWithWhile = False
        self.nonUtilizationElifElse = False
        self.elifRetestingCondition = False
        self.consecutiveEqualIfs = False
        self.repeatedCommandsInIfs = False
        self.unnecessaryElifElse = False
        self.sameBodyIfs = False
        # Categoria C
        self.whileCondInItsBody = False
        self.redundantLoop = False
        self.forWithConstant = False
        self.forVariableOverwritten = False
        self.redundantOpsInLoop = False
        # Categoria D
        self.varOutsideFuncScope = False
        # Categoria E
        self.listOverusage = False
        self.excessiveCombinationChecks = False
        # Categoria G
        self.nonSignificantNames = False
        self.arbitraryDeclarations = False
        # Categoria H
        self.noEffectStatement = False
        self._snapshot = None

    def prepare(self, root):
        """Coleta a árvore uma vez e instala somente uma referência imutável."""
        self._snapshot = ASTSnapshot.collect(root)
        return self

    def _nodes(self, root):
        """Retorna os nós da raiz já coletados, sem uma nova travessia."""
        if self._snapshot is not None and self._snapshot.root is root:
            return self._snapshot.nodes
        return tuple(ast.walk(root))

    def _nodes_of_type(self, node_type):
        if self._snapshot is None:
            return ()
        return self._snapshot.by_type.get(node_type, ())

    def reset(self):
        self.__init__()

    # =========================================================================
    # UTILITÁRIO INTERNO, TRAVESSIA ORDENADA
    # =========================================================================

    @staticmethod
    def _walk_ordered_stmts(stmts):
        """Componente do motor de análise estática do PC3."""
        for stmt in stmts:
            yield stmt
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue   # escopo separado, não desce
            for child_list in VisitorMC3._get_child_stmt_lists(stmt):
                yield from VisitorMC3._walk_ordered_stmts(child_list)

    @staticmethod
    def _get_child_stmt_lists(node):
        """Componente do motor de análise estática do PC3."""
        if isinstance(node, (ast.If, ast.For, ast.AsyncFor, ast.While)):
            yield node.body
            if node.orelse:
                yield node.orelse
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            yield node.body
        elif isinstance(node, ast.Try):
            yield node.body
            for handler in node.handlers:
                yield handler.body
            if node.orelse:
                yield node.orelse
            if node.finalbody:
                yield node.finalbody

    @staticmethod
    def _has_break_no_loop_all(stmts):
        """Retorna True quando a sequência contém um break alcançável em todos os caminhos considerados."""
        for stmt in stmts:
            if isinstance(stmt, ast.Break):
                return True
            if isinstance(stmt, ast.If):
                if VisitorMC3._all_paths_break(stmt):
                    return True
            # outras instruções (print, atribuição, etc.) não
            # garantem nem impedem break; continuamos verificando
            # as próximas instruções da sequência.
        return False

    @staticmethod
    def _all_paths_break(if_node):
        """Retorna True somente quando os ramos verdadeiro e falso do if terminam em break."""
        if_branch_breaks = VisitorMC3._has_break_no_loop_all(if_node.body)
        if not if_node.orelse:
            return False
        else_branch_breaks = VisitorMC3._has_break_no_loop_all(if_node.orelse)
        return if_branch_breaks and else_branch_breaks

    # =========================================================================
    # CATEGORIA A
    # =========================================================================

    def checkSelfAssignment(self, root):
        """PC3 A2, detecta atribuições que repetem exatamente a mesma referência no alvo e no valor.
        Compara alvos e valores por estrutura, incluindo atributos, subscritos e atribuições múltiplas."""
        self.selfAssignment = False

        def same_reference(a, b):
            if isinstance(a, ast.Name) and isinstance(b, ast.Name):
                return a.id == b.id
            if isinstance(a, ast.Attribute) and isinstance(b, ast.Attribute):
                return a.attr == b.attr and same_reference(a.value, b.value)
            if isinstance(a, ast.Subscript) and isinstance(b, ast.Subscript):
                return (same_reference(a.value, b.value) and
                        VisitorMC3Helper.compare_ast_nodes(a.slice, b.slice))
            if (isinstance(a, (ast.Tuple, ast.List)) and isinstance(b, (ast.Tuple, ast.List))
                    and len(a.elts) == len(b.elts)):
                return all(same_reference(ea, eb) for ea, eb in zip(a.elts, b.elts))
            return False

        for node in self._nodes(root):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if same_reference(target, node.value):
                        self.selfAssignment = True
                        return

    # -------------------------------------------------------------------------
    # A3, REESCRITA COMPLETA (v7)
    # -------------------------------------------------------------------------

    def checkUnusedInitVariables(self, root):
        """PC3 A3, identifica escritas iniciais que não são lidas antes de serem substituídas ou que nunca são usadas.
        Percorre as instruções em ordem e acompanha escritas pendentes e leituras em cada escopo."""
        self.unusedInitVar = False

        # ------------------------------------------------------------------
        # Núcleo: analisa uma lista de statements, atualizando used/pending.
        # Retorna True se uma misconception foi encontrada.
        # ------------------------------------------------------------------
        def _collect_reads(node, used, pending):
            """Componente do motor de análise estática do PC3."""
            def _lambda_bound_names(lam):
                names = set()
                a = lam.args
                for arglist in (getattr(a, "posonlyargs", []), a.args, a.kwonlyargs):
                    for arg in arglist:
                        names.add(arg.arg)
                if a.vararg:
                    names.add(a.vararg.arg)
                if a.kwarg:
                    names.add(a.kwarg.arg)
                return names

            def _comp_bound_names(comp_node):
                names = set()
                for gen in comp_node.generators:
                    for t in ast.walk(gen.target):
                        if isinstance(t, ast.Name):
                            names.add(t.id)
                return names

            def walk(n, shadowed):
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                    if n.id not in shadowed:
                        used.add(n.id)
                        pending.discard(n.id)
                    return
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    return  # barreira de escopo completa, não desce
                if isinstance(n, ast.Lambda):
                    walk(n.body, shadowed | _lambda_bound_names(n))
                    return
                if isinstance(n, (ast.ListComp, ast.SetComp,
                                   ast.GeneratorExp, ast.DictComp)):
                    bound = _comp_bound_names(n)
                    new_shadowed = shadowed | bound
                    if isinstance(n, ast.DictComp):
                        walk(n.key, new_shadowed)
                        walk(n.value, new_shadowed)
                    else:
                        walk(n.elt, new_shadowed)
                    for i, gen in enumerate(n.generators):
                        # o iterável do 1º gerador é avaliado no escopo
                        # externo; os demais (e os 'if's) já estão dentro
                        # do escopo da comprehension.
                        walk(gen.iter, shadowed if i == 0 else new_shadowed)
                        for cond in gen.ifs:
                            walk(cond, new_shadowed)
                    return
                for child in ast.iter_child_nodes(n):
                    walk(child, shadowed)

            walk(node, frozenset())

        def _collect_closure_free_reads(funcnode):
            """Componente do motor de análise estática do PC3."""
            assigned = set()
            reads = set()
            for n in ast.walk(funcnode):
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for arg in n.args.args:
                        assigned.add(arg.arg)
                if isinstance(n, ast.Name):
                    if isinstance(n.ctx, ast.Store):
                        assigned.add(n.id)
                    elif isinstance(n.ctx, ast.Load):
                        reads.add(n.id)
            return reads - assigned

        def _analyze_stmts(stmts, used, pending, is_function_scope=False):
            """Componente do motor de análise estática do PC3."""
            pending_at_entry = frozenset(pending)

            for stmt in stmts:

                #, Assign: lê RHS, depois escreve targets --
                if isinstance(stmt, ast.Assign):
                    # 1. Leituras no lado direito
                    _collect_reads(stmt.value, used, pending)
                    # 2. Cada target
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            var = target.id
                            if var in pending and var not in pending_at_entry:
                                # escrita sobre escrita sem leitura, DENTRO
                                # do mesmo bloco sequencial → morta de verdade
                                return True
                            if var not in used:
                                pending.add(var)
                        elif isinstance(target, (ast.Tuple, ast.List)):
                            for elt in target.elts:
                                if isinstance(elt, ast.Name):
                                    var = elt.id
                                    if var in pending and var not in pending_at_entry:
                                        return True
                                    if var not in used:
                                        pending.add(var)
                        else:
                            # atribuição a atributo/subscript: lê o alvo
                            _collect_reads(target, used, pending)

                #, AugAssign: lê e escreve (x += 1 implica leitura de x) --
                elif isinstance(stmt, ast.AugAssign):
                    if isinstance(stmt.target, ast.Name):
                        used.add(stmt.target.id)
                        pending.discard(stmt.target.id)
                    _collect_reads(stmt.value, used, pending)

                #, Return: registra leituras --
                elif isinstance(stmt, ast.Return):
                    if stmt.value is not None:
                        _collect_reads(stmt.value, used, pending)

                #, FunctionDef/AsyncFunctionDef aninhada: não desce, mas
                #    reconhece uso via closure --
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for name in _collect_closure_free_reads(stmt):
                        if name in pending:
                            used.add(name)
                            pending.discard(name)
                        used.add(name)

                #, If: analisa condição + branches independentes --
                elif isinstance(stmt, ast.If):
                    # condição é lida antes dos branches
                    _collect_reads(stmt.test, used, pending)

                    branches = [stmt.body]
                    if stmt.orelse:
                        branches.append(stmt.orelse)

                    branch_pendings = []
                    for branch in branches:
                        bp = set(pending)   # cópia independente
                        bu = set(used)
                        found = _analyze_stmts(branch, bu, bp, is_function_scope)
                        if found:
                            return True
                        used.update(bu)
                        branch_pendings.append(bp)

                    # pending ← interseção: só o que nunca foi lido em nenhum branch
                    if branch_pendings:
                        pending.clear()
                        pending.update(branch_pendings[0])
                        for bp in branch_pendings[1:]:
                            pending.intersection_update(bp)

                #, For/AsyncFor: analisa iter + body + orelse independentes --
                elif isinstance(stmt, (ast.For, ast.AsyncFor)):
                    _collect_reads(stmt.iter, used, pending)
                    # variável de iteração conta como escrita (não morta)
                    if isinstance(stmt.target, ast.Name):
                        pending.discard(stmt.target.id)
                        used.add(stmt.target.id)
                    elif isinstance(stmt.target, (ast.Tuple, ast.List)):
                        for elt in stmt.target.elts:
                            if isinstance(elt, ast.Name):
                                pending.discard(elt.id)
                                used.add(elt.id)

                    branches = [stmt.body]
                    if stmt.orelse:
                        branches.append(stmt.orelse)

                    branch_pendings = []
                    for branch in branches:
                        bp = set(pending)
                        bu = set(used)
                        found = _analyze_stmts(branch, bu, bp, is_function_scope)
                        if found:
                            return True
                        used.update(bu)
                        branch_pendings.append(bp)

                    if branch_pendings:
                        pending.clear()
                        pending.update(branch_pendings[0])
                        for bp in branch_pendings[1:]:
                            pending.intersection_update(bp)

                #, While: analisa condição + body + orelse --
                elif isinstance(stmt, ast.While):
                    _collect_reads(stmt.test, used, pending)

                    branches = [stmt.body]
                    if stmt.orelse:
                        branches.append(stmt.orelse)

                    branch_pendings = []
                    for branch in branches:
                        bp = set(pending)
                        bu = set(used)
                        found = _analyze_stmts(branch, bu, bp, is_function_scope)
                        if found:
                            return True
                        used.update(bu)
                        branch_pendings.append(bp)

                    if branch_pendings:
                        pending.clear()
                        pending.update(branch_pendings[0])
                        for bp in branch_pendings[1:]:
                            pending.intersection_update(bp)

                #, Try: trata cada bloco como branch independente --
                elif isinstance(stmt, ast.Try):
                    branches = [stmt.body]
                    for handler in stmt.handlers:
                        branches.append(handler.body)
                    if stmt.orelse:
                        branches.append(stmt.orelse)
                    # finalbody sempre executa, processa em sequência depois
                    finally_stmts = stmt.finalbody if stmt.finalbody else []

                    branch_pendings = []
                    for branch in branches:
                        bp = set(pending)
                        bu = set(used)
                        found = _analyze_stmts(branch, bu, bp, is_function_scope)
                        if found:
                            return True
                        used.update(bu)
                        branch_pendings.append(bp)

                    if branch_pendings:
                        pending.clear()
                        pending.update(branch_pendings[0])
                        for bp in branch_pendings[1:]:
                            pending.intersection_update(bp)

                    if finally_stmts:
                        found = _analyze_stmts(finally_stmts, used, pending,
                                               is_function_scope)
                        if found:
                            return True

                #, With/AsyncWith: analisa context managers + body --
                elif isinstance(stmt, (ast.With, ast.AsyncWith)):
                    for item in stmt.items:
                        _collect_reads(item.context_expr, used, pending)
                        if item.optional_vars is not None:
                            if isinstance(item.optional_vars, ast.Name):
                                pending.discard(item.optional_vars.id)
                                used.add(item.optional_vars.id)
                    found = _analyze_stmts(stmt.body, used, pending,
                                           is_function_scope)
                    if found:
                        return True

                #, Qualquer outro stmt: apenas registra leituras --
                else:
                    _collect_reads(stmt, used, pending)

            return False

        all_file_reads = set()
        for n in ast.walk(root):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                all_file_reads.add(n.id)
            elif isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
                all_file_reads.add(n.target.id)

        # 2. Statements top-level (sem FunctionDef/AsyncFunctionDef)
        global_stmts = [
            node for node in ast.iter_child_nodes(root)
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        # A) Detecção de escrita morta, used começa vazio
        global_used_dw    = set()
        global_pending_dw = set()
        if _analyze_stmts(global_stmts, global_used_dw, global_pending_dw,
                          is_function_scope=False):
            self.unusedInitVar = True
            return

        # B) Detecção de variável jamais lida em nenhum lugar do arquivo
        global_declared = set()
        for node in global_stmts:
            for chd in ast.walk(node):
                if isinstance(chd, ast.Assign):
                    for t in chd.targets:
                        if isinstance(t, ast.Name):
                            global_declared.add(t.id)
                        elif isinstance(t, (ast.Tuple, ast.List)):
                            for elt in t.elts:
                                if isinstance(elt, ast.Name):
                                    global_declared.add(elt.id)

        if global_declared - all_file_reads:
            self.unusedInitVar = True
            return

        def _collect_global_nonlocal_names(funcNode):
            names = set()
            for n in VisitorMC3._iter_own_scope_nodes(funcNode):
                if n is funcNode:
                    continue
                if isinstance(n, (ast.Global, ast.Nonlocal)):
                    names.update(n.names)
            return names

        for node in self._nodes(root):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue

            func_used    = set()
            func_pending = set()

            # Parâmetros já são "conhecidos", não são escritas pendentes
            for arg in node.args.args:
                func_used.add(arg.arg)

            # Nomes 'global'/'nonlocal' pertencem a outro escopo, não são
            # escritas locais pendentes de leitura nesta função.
            func_used.update(_collect_global_nonlocal_names(node))

            if _analyze_stmts(node.body, func_used, func_pending,
                               is_function_scope=True):
                self.unusedInitVar = True
                return

            # Variáveis declaradas na função mas nunca lidas
            if func_pending:
                self.unusedInitVar = True
                return

    def checkBuiltInRedefinition(self, root):
        """PC3 A4, identifica nomes de variáveis, funções e parâmetros que sombreiam nomes built-in do Python.
        Coleta declarações em atribuições, parâmetros, laços, with, exceções e comprehensions."""
        list_of_builtins = {
            'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes',
            'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr',
            'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter',
            'float', 'format', 'frozenset', 'getattr', 'global', 'hasattr',
            'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
            'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next',
            'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr',
            'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
            'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
        }

        def add_var_target(tgt):
            if isinstance(tgt, ast.Name):
                if tgt.id in list_of_builtins:
                    self.declaredVariablesAsBuiltIn.add(tgt.id)
            elif isinstance(tgt, (ast.Tuple, ast.List)):
                for elt in tgt.elts:
                    add_var_target(elt)

        def add_param(arg):
            if arg is not None and arg.arg in list_of_builtins:
                self.declaredArgumentsAsBuiltin.add(arg.arg)

        def add_all_params(args_node):
            for arglist in (getattr(args_node, "posonlyargs", []),
                            args_node.args, args_node.kwonlyargs):
                for a in arglist:
                    add_param(a)
            if args_node.vararg:
                add_param(args_node.vararg)
            if args_node.kwarg:
                add_param(args_node.kwarg)

        for node in self._nodes(root):
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    add_var_target(tgt)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name in list_of_builtins:
                    self.declaredFunctionsAsBuiltin.add(node.name)
                add_all_params(node.args)
            elif isinstance(node, ast.Lambda):
                add_all_params(node.args)
            elif isinstance(node, (ast.For, ast.AsyncFor)):
                add_var_target(node.target)
            elif isinstance(node, (ast.With, ast.AsyncWith)):
                for item in node.items:
                    if item.optional_vars is not None:
                        add_var_target(item.optional_vars)
            elif isinstance(node, ast.ExceptHandler):
                if node.name and node.name in list_of_builtins:
                    self.declaredVariablesAsBuiltIn.add(node.name)
            elif isinstance(node, ast.comprehension):
                add_var_target(node.target)

        if (len(self.declaredVariablesAsBuiltIn) +
                len(self.declaredFunctionsAsBuiltin) +
                len(self.declaredArgumentsAsBuiltin) > 0):
            self.builtinRedefinition = True

    def checkUnusedImports(self, root):
        """PC3 A5, identifica imports declarados que não aparecem em uma leitura no código.
        Conta um import como usado somente quando o nome aparece em contexto de leitura."""
        import_names = set()
        used_names   = set()

        for node in self._nodes(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_names.add(alias.asname or alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == '*':
                        continue
                    import_names.add(alias.asname or alias.name)

        for node in self._nodes(root):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_names.add(node.id)

        self.unusedImports = list(import_names - used_names)

    # =========================================================================
    # CATEGORIA B
    # =========================================================================

    def checkRepeatedCommandsInIfs(self, root):
        """PC3 B4, identifica comandos idênticos repetidos nos ramos de uma cadeia if, elif e else.
        Compara os corpos de uma mesma cadeia e ignora guard clauses triviais."""
        def is_trivial_guard(body):
            return (len(body) == 1 and
                    isinstance(body[0], (ast.Return, ast.Raise,
                                          ast.Continue, ast.Break, ast.Pass)))

        def check_if_chain(node):
            """Auxiliar do PC3 B4, reúne os corpos de uma cadeia condicional para comparação."""
            blocks = []
            current = node
            while isinstance(current, ast.If):
                blocks.append(current.body)
                if len(current.orelse) == 1 and isinstance(current.orelse[0], ast.If):
                    current = current.orelse[0]
                else:
                    if current.orelse:
                        blocks.append(current.orelse)
                    break
            block_sources = ["|".join([ast.dump(s) for s in body]) for body in blocks
                              if not is_trivial_guard(body)]
            seen = set()
            for src in block_sources:
                if src in seen:
                    return True
                seen.add(src)
            return False

        def walk_for_ifs(node):
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If):
                    if check_if_chain(child):
                        self.repeatedCommandsInIfs = True
                        return
                    walk_for_ifs(child)
                else:
                    walk_for_ifs(child)

        walk_for_ifs(root)

    def checkBooleanAttemptedWithWhile(self, root):
        """PC3 B6, identifica while usado como se fosse uma seleção condicional simples.
        Verifica a forma da condição e se o corpo do laço possui saída garantida."""
        for node in self._nodes(root):
            if not isinstance(node, ast.While):
                continue
            test = node.test
            is_boolean_like = isinstance(test, (ast.Compare, ast.BoolOp, ast.Name)) or (
                isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not)
            )
            if not is_boolean_like:
                continue
            if not node.body:
                continue

            last_stmt = node.body[-1]
            unconditional_break_at_end = False

            if isinstance(last_stmt, ast.Break):
                unconditional_break_at_end = True
            elif isinstance(last_stmt, ast.If):
                if VisitorMC3._all_paths_break(last_stmt):
                    unconditional_break_at_end = True

            if unconditional_break_at_end:
                self.boolOpAttemptedWithWhile = True
                return

    def checkNonUtilizationElifElse(self, root):
        """PC3 B8, identifica cadeias condicionais sem elif ou else quando a estrutura sugere um fluxo incompleto.
        Examina a estrutura dos ramos e sinaliza cadeias que não tratam alternativas relevantes."""
        self.nonUtilizationElifElse = False
        for node in self._nodes(root):
            if isinstance(node, ast.If):
                current = node
                while True:
                    if not current.orelse:
                        self.nonUtilizationElifElse = True
                        return
                    if not isinstance(current.orelse[0], ast.If):
                        break  # tem 'else' de verdade, cadeia termina corretamente
                    current = current.orelse[0]

    def checkElifRetestingCondition(self, root):
        """PC3 B9, identifica elif que testa novamente uma condição já coberta pelo if anterior.
        Compara testes de if e elif, incluindo comparações equivalentes e negações."""
        def compareElifsR(node, mainLeft, mainOps, mainCps):
            if isinstance(node, ast.Compare):
                if (VisitorMC3Helper.compare_ast_nodes(mainLeft, node.left) and
                        VisitorMC3Helper.compare_ops_inverse(mainOps, node.ops) and
                        VisitorMC3Helper.compare_comparators(mainCps, node.comparators)):
                    self.elifRetestingCondition = True
                    return
            if isinstance(node, ast.BoolOp):
                for chd in node.values:
                    compareElifsR(chd, mainLeft, mainOps, mainCps)

        def _negate_compare(cmp_node):
            # Só nega comparações de um único operador; encadeadas
            # (a < b < c) não têm negação direta de operador único.
            if not isinstance(cmp_node, ast.Compare) or len(cmp_node.ops) != 1:
                return None
            inv_op_cls = VisitorMC3Helper.get_inverse_op(cmp_node.ops[0])
            if inv_op_cls is None:
                return None
            return ast.Compare(left=cmp_node.left, ops=[inv_op_cls()],
                                comparators=cmp_node.comparators)

        def _negate_test(test):
            if isinstance(test, ast.Compare):
                return _negate_compare(test)
            if isinstance(test, ast.BoolOp):
                inv_op = ast.Or() if isinstance(test.op, ast.And) else ast.And()
                negated_values = []
                for v in test.values:
                    nv = _negate_test(v)
                    if nv is None:
                        return None
                    negated_values.append(nv)
                return ast.BoolOp(op=inv_op, values=negated_values)
            if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
                return test.operand
            return None

        for node in self._nodes(root):
            if isinstance(node, ast.If):
                if len(node.orelse) == 0:
                    continue
                if isinstance(node.test, ast.Compare):
                    for chd in node.orelse:
                        if isinstance(chd, ast.If):
                            compareElifsR(chd.test, node.test.left,
                                          node.test.ops, node.test.comparators)
                            if self.elifRetestingCondition:
                                return
                elif isinstance(node.test, ast.BoolOp):
                    negated_main = _negate_test(node.test)
                    if negated_main is None:
                        continue
                    negated_dump = ast.dump(negated_main)
                    for chd in node.orelse:
                        if isinstance(chd, ast.If) and ast.dump(chd.test) == negated_dump:
                            self.elifRetestingCondition = True
                            return

    def checkUnnecessaryElifElse(self, root):
        """PC3 B10, identifica ramos elif ou else vazios ou contendo apenas pass."""
        def is_empty_or_pass_only(body):
            if not body:
                return True
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                return True
            return False

        for node in self._nodes(root):
            if isinstance(node, ast.If):
                if is_empty_or_pass_only(node.body) and node.orelse:
                    self.unnecessaryElifElse = True
                    return
                if node.orelse:
                    if isinstance(node.orelse[0], ast.If):
                        if is_empty_or_pass_only(node.orelse[0].body):
                            self.unnecessaryElifElse = True
                            return
                    else:
                        # 'else' de verdade (não elif), checa se está vazio/pass-only
                        if is_empty_or_pass_only(node.orelse):
                            self.unnecessaryElifElse = True
                            return

    def checkIfsWithSameBody(self, root):
        """PC3 B11, identifica ifs independentes com corpos não triviais estruturalmente idênticos."""
        self.sameBodyIfs = False

        def is_trivial_guard(body):
            return (len(body) == 1 and
                    isinstance(body[0], (ast.Return, ast.Raise,
                                          ast.Continue, ast.Break, ast.Pass)))

        def check_scope(node):
            """Auxiliar do PC3 B11, percorre um escopo e compara corpos de ifs irmãos."""
            seen_bodies = {}
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If):
                    if not is_trivial_guard(child.body):
                        body_repr = "|".join([ast.dump(s) for s in child.body])
                        if body_repr in seen_bodies:
                            self.sameBodyIfs = True
                            return
                        seen_bodies[body_repr] = True
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef,
                                      ast.For, ast.AsyncFor, ast.While,
                                      ast.With, ast.AsyncWith,
                                      ast.If, ast.Try, ast.ClassDef)):
                    check_scope(child)
                    if self.sameBodyIfs:
                        return

        check_scope(root)

    def checkConsecutiveIfs(self, root):
        """PC3 B12, identifica ifs consecutivos com a mesma condição e ações diferentes."""
        def same_test(a, b):
            if isinstance(a, ast.Name) and isinstance(b, ast.Name):
                return a.id == b.id
            if isinstance(a, ast.Compare) and isinstance(b, ast.Compare):
                L = VisitorMC3Helper.compare_ast_nodes(a.left, b.left)
                O = VisitorMC3Helper.compare_ops_equal(a.ops, b.ops)
                R = VisitorMC3Helper.compare_comparators(a.comparators, b.comparators)
                return L and O and R
            return False

        for node in self._nodes(root):
            conseqIf = False
            firstIf  = None
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If):
                    if conseqIf:
                        if len(child.orelse) == 0:
                            secondIf = child
                            if same_test(firstIf.test, secondIf.test):
                                self.consecutiveEqualIfs = True
                                return
                            # não bateu: secondIf vira o novo firstIf,
                            # para permitir comparar com o próximo child
                            firstIf  = secondIf
                            conseqIf = True
                        else:
                            conseqIf = False
                    else:
                        if len(child.orelse) == 0:
                            conseqIf = True
                            firstIf  = child
                else:
                    conseqIf = False

    # =========================================================================
    # CATEGORIA C
    # =========================================================================

    def checkWhileCondInItsBody(self, root):
        """PC3 C1, identifica a repetição da condição do while dentro do próprio corpo do laço.
        Procura referências à própria condição dentro do corpo de cada while."""
        for node in self._nodes(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Compare):
                    for item in VisitorMC3._walk_ordered_stmts(node.body):
                        if isinstance(item, ast.If) and isinstance(item.test, ast.Compare):
                            L = VisitorMC3Helper.compare_ast_nodes(
                                node.test.left, item.test.left)
                            O = VisitorMC3Helper.compare_ops_inverse(
                                node.test.ops, item.test.ops)
                            R = VisitorMC3Helper.compare_comparators(
                                node.test.comparators, item.test.comparators)
                            if L and O and R:
                                self.whileCondInItsBody = True
                                return

    def checkRedundantLoop(self, root):
        """PC3 C2, identifica laços que não acrescentam iterações úteis ou que terminam imediatamente.
        Sinaliza while True com break garantido e for range(1), que não oferecem iteração útil."""
        for node in self._nodes(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Constant) and node.test.value is True:
                    if VisitorMC3._has_break_no_loop_all(node.body):
                        self.redundantLoop = True
                        return
        for node in self._nodes(root):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    if (isinstance(node.iter.func, ast.Name) and
                            node.iter.func.id == "range"):
                        if len(node.iter.args) == 1:
                            if isinstance(node.iter.args[0], ast.Constant):
                                if node.iter.args[0].value == 1:
                                    self.redundantLoop = True
                                    return

    def checkRedundantOpsInLoop(self, root):
        """PC3 C3, identifica operações idênticas repetidas no mesmo bloco de um laço.
        Compara atribuições, expressões e atribuições aumentadas no mesmo bloco do laço."""
        def has_duplicate_in_block(stmts):
            seen = set()
            for stmt in stmts:
                if isinstance(stmt, (ast.Assign, ast.Expr, ast.AugAssign)):
                    code_repr = ast.dump(stmt)
                    if code_repr in seen:
                        return True
                    seen.add(code_repr)
            for stmt in stmts:
                for child_list in VisitorMC3._get_child_stmt_lists(stmt):
                    if has_duplicate_in_block(child_list):
                        return True
            return False

        for node in self._nodes(root):
            if isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
                if has_duplicate_in_block(node.body):
                    self.redundantOpsInLoop = True
                    return

    def checkForWithConstant(self, root, constThreshold=50):
        """PC3 C4, identifica for baseado em range constante a partir do limite configurado.
        Resolve as formas de range com um, dois ou três argumentos, incluindo passo negativo."""
        for node in self._nodes(root):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    func = node.iter.func
                    if isinstance(func, ast.Name) and func.id == "range":
                        args = node.iter.args

                        if len(args) == 1:
                            limit_arg = args[0]
                        elif len(args) == 2:
                            limit_arg = args[1]
                        elif len(args) == 3:
                            step = args[2]
                            # Resolve o valor numérico do step.
                            # -1 literal é representado pelo parser como
                            # UnaryOp(USub, Constant(1)), não como Constant(-1),
                            # portanto é necessário tratar os dois casos.
                            step_val = None
                            if (isinstance(step, ast.Constant) and
                                    isinstance(step.value, (int, float))):
                                step_val = step.value
                            elif (isinstance(step, ast.UnaryOp) and
                                    isinstance(step.op, ast.USub) and
                                    isinstance(step.operand, ast.Constant) and
                                    isinstance(step.operand.value, (int, float))):
                                step_val = -step.operand.value
                            if step_val is not None and step_val < 0:
                                limit_arg = args[0]
                            else:
                                limit_arg = args[1]
                        else:
                            continue

                        if isinstance(limit_arg, ast.Constant):
                            if limit_arg.value >= constThreshold:
                                self.forWithConstant = True
                                return

    def checkForOverwritten(self, root, prevIterVars=None):
        """PC3 C8, identifica a sobrescrita da variável de iteração dentro do próprio for.
        Percorre blocos aninhados e compara atribuições com as variáveis de iteração ativas."""
        if prevIterVars is None:
            prevIterVars = []

        def getVarIter(node):
            varIter = []
            if isinstance(node.target, ast.Name):
                varIter.append(node.target.id)
            elif isinstance(node.target, (ast.Tuple, ast.List)):
                for item in node.target.elts:
                    if isinstance(item, ast.Name):
                        varIter.append(item.id)
            return varIter

        def check_body(stmts, all_iter_vars):
            """Auxiliar do PC3 C8, acompanha variáveis de iteração nos blocos aninhados."""
            for stmt in stmts:
                if isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            if target.id in all_iter_vars:
                                return True
                        elif isinstance(target, ast.Tuple):
                            for elem in target.elts:
                                if isinstance(elem, ast.Name):
                                    if elem.id in all_iter_vars:
                                        return True
                elif isinstance(stmt, ast.AugAssign):
                    if isinstance(stmt.target, ast.Name):
                        if stmt.target.id in all_iter_vars:
                            return True
                elif isinstance(stmt, (ast.For, ast.AsyncFor)):
                    nested_iter_vars = all_iter_vars + getVarIter(stmt)
                    if check_body(stmt.body, nested_iter_vars):
                        return True
                    continue  # já desceu no corpo deste for; não repetir abaixo
                for child_list in VisitorMC3._get_child_stmt_lists(stmt):
                    if check_body(child_list, all_iter_vars):
                        return True
            return False

        for node in self._nodes(root):
            if isinstance(node, (ast.For, ast.AsyncFor)):
                varIter       = getVarIter(node)
                all_iter_vars = prevIterVars + varIter
                if check_body(node.body, all_iter_vars):
                    self.forVariableOverwritten = True
                    return

    # =========================================================================
    # CATEGORIA D
    # =========================================================================

    @staticmethod
    def _iter_own_scope_nodes(funcNode):
        """Componente do motor de análise estática do PC3."""
        stack = [funcNode]
        while stack:
            n = stack.pop()
            yield n
            for child in ast.iter_child_nodes(n):
                if child is funcNode:
                    continue
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                stack.append(child)

    def checkVarOutsideFuncScope(self, root):
        """PC3 D4, identifica o uso de variáveis globais dentro de funções sem declaração local correspondente.
        Coleta nomes globais e locais e examina leituras em expressões executadas dentro de funções."""
        def getGlobalVars(root):
            globalVars = set()
            for node in ast.iter_child_nodes(root):
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for chd in ast.walk(node):
                        if isinstance(chd, ast.Assign):
                            for item in chd.targets:
                                if isinstance(item, ast.Name):
                                    globalVars.add(item.id)
                                elif isinstance(item, ast.Tuple):
                                    for elem in item.elts:
                                        if isinstance(elem, ast.Name):
                                            globalVars.add(elem.id)
            return globalVars

        def getLocalVars(funcNode):
            localVars = set()
            declaredGlobalNonlocal = set()
            for arg in funcNode.args.args:
                localVars.add(arg.arg)
            for node in VisitorMC3._iter_own_scope_nodes(funcNode):
                if isinstance(node, ast.Assign):
                    for item in node.targets:
                        if isinstance(item, ast.Name):
                            localVars.add(item.id)
                        elif isinstance(item, ast.Tuple):
                            for elem in item.elts:
                                if isinstance(elem, ast.Name):
                                    localVars.add(elem.id)
                elif isinstance(node, ast.AugAssign):
                    if isinstance(node.target, ast.Name):
                        localVars.add(node.target.id)
                elif isinstance(node, (ast.Global, ast.Nonlocal)):
                    declaredGlobalNonlocal.update(node.names)
            # nomes 'global'/'nonlocal' nunca são locais, mesmo que também
            # sejam alvo de atribuição em algum ponto do corpo
            localVars -= declaredGlobalNonlocal
            return localVars

        def checkNameUsage(nameNode, localVars, globalVars):
            """Auxiliar do PC3 D4, verifica se um nome lido pertence ao escopo global."""
            if isinstance(nameNode, ast.Name):
                if nameNode.id in globalVars and nameNode.id not in localVars:
                    self.varOutsideFuncScope = True
                    return True
            return False

        def checkVarUsage(stm, localVars, globalVars):
            """Auxiliar do PC3 D4, percorre expressões executáveis e encaminha leituras para a verificação de escopo."""
            if isinstance(stm, ast.BinOp):
                if checkNameUsage(stm.left, localVars, globalVars):  return
                if checkNameUsage(stm.right, localVars, globalVars): return
            if isinstance(stm, ast.UnaryOp):
                if checkNameUsage(stm.operand, localVars, globalVars): return
            if isinstance(stm, ast.Expr) and isinstance(stm.value, ast.Call):
                if isinstance(stm.value.func, ast.Attribute):
                    if isinstance(stm.value.func.value, ast.Name):
                        if checkNameUsage(stm.value.func.value, localVars, globalVars): return
                for arg in stm.value.args:
                    for node in ast.walk(arg):
                        if checkNameUsage(node, localVars, globalVars): return
                for kw in stm.value.keywords:
                    for node in ast.walk(kw.value):
                        if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Assign):
                for target in stm.targets:
                    for node in ast.walk(target):
                        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                            if checkNameUsage(node, localVars, globalVars): return
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.AugAssign):
                for node in ast.walk(stm.target):
                    if isinstance(node, ast.Name):
                        if checkNameUsage(node, localVars, globalVars): return
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, (ast.If, ast.While)):
                for node in ast.walk(stm.test):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, (ast.For, ast.AsyncFor)):
                for node in ast.walk(stm.iter):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Return) and stm.value is not None:
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Assert):
                for node in ast.walk(stm.test):
                    if checkNameUsage(node, localVars, globalVars): return
                if stm.msg is not None:
                    for node in ast.walk(stm.msg):
                        if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.With):
                for item in stm.items:
                    for node in ast.walk(item.context_expr):
                        if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Raise):
                if stm.exc is not None:
                    for node in ast.walk(stm.exc):
                        if checkNameUsage(node, localVars, globalVars): return
                if stm.cause is not None:
                    for node in ast.walk(stm.cause):
                        if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Delete):
                for target in stm.targets:
                    for node in ast.walk(target):
                        if checkNameUsage(node, localVars, globalVars): return

        globalVars = getGlobalVars(root)
        for node in self._nodes(root):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                localVars = getLocalVars(node)
                for stm in VisitorMC3._iter_own_scope_nodes(node):
                    if stm is node:
                        continue
                    checkVarUsage(stm, localVars, globalVars)
                    if self.varOutsideFuncScope:
                        return

    # =========================================================================
    # CATEGORIA E
    # =========================================================================

    def checkAllCombinationsRedundancy(self, root):
        """PC3 E1, identifica condições longas e cadeias que enumeram combinações de átomos booleanos.
        Avalia o padrão de condição longa e também cadeias que cobrem todas as combinações."""
        self.excessiveCombinationChecks = False

        # --- padrão (a): condição única com BoolOp grande ---
        for node in self._nodes(root):
            if isinstance(node, ast.If) and isinstance(node.test, ast.BoolOp):
                if isinstance(node.test.op, (ast.And, ast.Or)):
                    if len(node.test.values) > 5:
                        self.excessiveCombinationChecks = True
                        return

        # --- padrão (b): cadeia de if/elif cobrindo todas as combinações ---
        def split_conjuncts(test):
            if isinstance(test, ast.BoolOp) and isinstance(test.op, ast.And):
                result = []
                for v in test.values:
                    result.extend(split_conjuncts(v))
                return result
            return [test]

        def has_or(test):
            return any(isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or)
                       for n in ast.walk(test))

        _CANONICAL_OP_ORDER = (ast.Eq, ast.Lt, ast.LtE, ast.In, ast.Is)

        def normalize_atom(expr):
            if isinstance(expr, ast.UnaryOp) and isinstance(expr.op, ast.Not):
                atom_id, negated = normalize_atom(expr.operand)
                return atom_id, not negated
            if isinstance(expr, ast.Compare) and len(expr.ops) == 1 and len(expr.comparators) == 1:
                op_type = type(expr.ops[0])
                inverse_op = VisitorMC3Helper.get_inverse_op(expr.ops[0])
                if inverse_op is not None:
                    if op_type in _CANONICAL_OP_ORDER:
                        canonical_op, negated = op_type, False
                    else:
                        canonical_op, negated = inverse_op, True
                    canonical_node = ast.Compare(left=expr.left, ops=[canonical_op()],
                                                  comparators=expr.comparators)
                    return ast.dump(canonical_node), negated
            return ast.dump(expr), False

        def get_chain_tests(if_node):
            tests = []
            node = if_node
            while True:
                tests.append(node.test)
                if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
                    node = node.orelse[0]
                else:
                    break
            return tests

        for node in self._nodes(root):
            if not isinstance(node, ast.If):
                continue
            tests = get_chain_tests(node)
            if len(tests) < 4 or any(has_or(t) for t in tests):
                continue

            atoms = None
            branch_sets = []
            valid = True
            for t in tests:
                normalized = [normalize_atom(c) for c in split_conjuncts(t)]
                atom_ids = [a for a, _ in normalized]
                if len(set(atom_ids)) != len(atom_ids):
                    valid = False
                    break
                branch_atoms = frozenset(atom_ids)
                if atoms is None:
                    atoms = branch_atoms
                elif branch_atoms != atoms:
                    valid = False
                    break
                branch_sets.append(frozenset(normalized))

            if not valid or atoms is None:
                continue
            n = len(atoms)
            if n < 2 or len(tests) != 2 ** n:
                continue
            if len(set(branch_sets)) != len(tests):
                continue  # ramos duplicados: não é cobertura completa distinta

            self.excessiveCombinationChecks = True
            return

    def checkListOverusage(self, root, numListThreshold=5):
        """PC3 E2, identifica quantidade de listas declaradas a partir do limite configurado.
        Conta listas literais, comprehensions, chamadas list e atribuições anotadas."""
        def is_list_creation(value):
            if isinstance(value, (ast.List, ast.ListComp)):
                return True
            if (isinstance(value, ast.Call) and isinstance(value.func, ast.Name)
                    and value.func.id == "list"):
                return True
            return False

        numLists = 0
        for node in self._nodes(root):
            if isinstance(node, ast.Assign):
                if is_list_creation(node.value):
                    numLists += 1
            elif isinstance(node, ast.AnnAssign):
                if node.value is not None and is_list_creation(node.value):
                    numLists += 1
        if numLists >= numListThreshold:
            self.listOverusage = True

    # =========================================================================
    # CATEGORIA G
    # =========================================================================

    def checkNonSignificantNames(self, root, varLenThreshold, funcLenThreshold,
                                  totalNamesThreshold):
        """PC3 G4, identifica concentração elevada de nomes curtos ou pouco descritivos.
        Calcula a proporção de nomes curtos entre variáveis, funções e parâmetros."""
        EXCLUDED_PARAMS = {'self', 'cls'}
        EXCLUDED_VARS   = {'_'}

        def collectVariableNames(root):
            names = []
            for node in self._nodes(root):
                if isinstance(node, ast.Assign):
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            if tgt.id not in EXCLUDED_VARS and tgt.id not in names:
                                names.append(tgt.id)
                        if isinstance(tgt, ast.Tuple):
                            for item in tgt.elts:
                                if isinstance(item, ast.Name):
                                    if item.id not in EXCLUDED_VARS and item.id not in names:
                                        names.append(item.id)
            return names

        def isDunderMethod(name):
            """Componente do motor de análise estática do PC3."""
            return name.startswith("__") and name.endswith("__") and len(name) > 4

        def collectFunctionNames(root):
            names = []
            for node in self._nodes(root):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if node.name not in names and not isDunderMethod(node.name):
                        names.append(node.name)
            return names

        def collectParamNames(root):
            names = []
            for node in self._nodes(root):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for arg in node.args.args:
                        if arg.arg not in EXCLUDED_PARAMS and arg.arg not in names:
                            names.append(arg.arg)
            return names

        def calculateNameLengthTotals(names):
            lengths = {}
            for name in names:
                length = len(name)
                lengths[length] = lengths.get(length, 0) + 1
            return lengths

        def checkNames(names, nameThreshold, totalThreshold):
            """Auxiliar do PC3 G4, calcula a proporção de nomes abaixo do limite configurado."""
            if not names:
                return False
            totalNames = len(names)
            totalNonSignificant = sum(
                count for length, count in calculateNameLengthTotals(names).items()
                if length <= nameThreshold
            )
            return totalNonSignificant >= totalNames * totalThreshold / 100

        varNames   = collectVariableNames(root)
        funcNames  = collectFunctionNames(root)
        paramNames = collectParamNames(root)

        if checkNames(varNames, varLenThreshold, totalNamesThreshold):
            self.nonSignificantNames = True
        elif checkNames(funcNames, funcLenThreshold, totalNamesThreshold):
            self.nonSignificantNames = True
        elif checkNames(paramNames, varLenThreshold, totalNamesThreshold):
            self.nonSignificantNames = True

    def checkArbitraryDeclarations(self, root):
        """PC3 G5, identifica declarações de funções ou classes depois de código executável no mesmo escopo.
        Percorre declarações no escopo do módulo e procura código executável antes de funções ou classes."""
        self.arbitraryDeclarations = False
        found_executable_code = False

        for node in ast.iter_child_nodes(root):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                continue
            if VisitorMC3Helper.is_block_comment(node):
                continue
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if found_executable_code:
                    self.arbitraryDeclarations = True
                    return
            else:
                found_executable_code = True

    # =========================================================================
    # CATEGORIA H
    # =========================================================================

    def checkNoEffectStatement(self, root):
        """PC3 H1, identifica expressões isoladas que não produzem efeito observável.
        Ignora strings usadas como comentários de bloco e sinaliza expressões sem efeito."""
        NO_EFFECT_EXPR_TYPES = (ast.Compare, ast.Name, ast.BinOp, ast.BoolOp, ast.UnaryOp)
        for node in self._nodes(root):
            if isinstance(node, ast.Expr):
                value = node.value
                if isinstance(value, ast.Constant):
                    if isinstance(value.value, str) or value.value is Ellipsis:
                        continue
                    self.noEffectStatement = True
                    return
                if isinstance(value, NO_EFFECT_EXPR_TYPES):
                    self.noEffectStatement = True
                    return

    # =========================================================================
    # INTERFACE PÚBLICA, MÉTODOS GET
    # =========================================================================

    def analyze_all(self, root, config=None):
        """Executa todos os detectores após uma única coleta da AST.

        Cada regra recebe um visitor novo, mas todos recebem o mesmo
        ``ASTSnapshot`` imutável. Assim, flags e coleções nunca vazam entre
        regras, sem repetir a travessia principal da árvore.
        """
        config = config or MC3Config()
        snapshot = ASTSnapshot.collect(root)
        specs = {
            'A2': ('checkSelfAssignment', (), 'selfAssignment'),
            'A3': ('checkUnusedInitVariables', (), 'unusedInitVar'),
            'A4': ('checkBuiltInRedefinition', (), None),
            'A5': ('checkUnusedImports', (), None),
            'B4': ('checkRepeatedCommandsInIfs', (), 'repeatedCommandsInIfs'),
            'B6': ('checkBooleanAttemptedWithWhile', (), 'boolOpAttemptedWithWhile'),
            'B8': ('checkNonUtilizationElifElse', (), 'nonUtilizationElifElse'),
            'B9': ('checkElifRetestingCondition', (), 'elifRetestingCondition'),
            'B10': ('checkUnnecessaryElifElse', (), 'unnecessaryElifElse'),
            'B11': ('checkIfsWithSameBody', (), 'sameBodyIfs'),
            'B12': ('checkConsecutiveIfs', (), 'consecutiveEqualIfs'),
            'C1': ('checkWhileCondInItsBody', (), 'whileCondInItsBody'),
            'C2': ('checkRedundantLoop', (), 'redundantLoop'),
            'C3': ('checkRedundantOpsInLoop', (), 'redundantOpsInLoop'),
            'C4': ('checkForWithConstant', (config.c4_range_threshold,), 'forWithConstant'),
            'C8': ('checkForOverwritten', ([],), 'forVariableOverwritten'),
            'D4': ('checkVarOutsideFuncScope', (), 'varOutsideFuncScope'),
            'E1': ('checkAllCombinationsRedundancy', (), 'excessiveCombinationChecks'),
            'E2': ('checkListOverusage', (config.e2_list_threshold,), 'listOverusage'),
            'G4': ('checkNonSignificantNames', (config.g4_min_var_chars,
                                                 config.g4_min_func_chars,
                                                 config.g4_max_nonsignificant_percent),
                   'nonSignificantNames'),
            'G5': ('checkArbitraryDeclarations', (), 'arbitraryDeclarations'),
            'H1': ('checkNoEffectStatement', (), 'noEffectStatement'),
        }
        results = {}
        for name, (method_name, args, attr) in specs.items():
            worker = VisitorMC3()
            worker._snapshot = snapshot
            getattr(worker, method_name)(root, *args)
            if name == 'A4':
                results[name] = (worker.builtinRedefinition,
                                 list(worker.declaredVariablesAsBuiltIn),
                                 list(worker.declaredFunctionsAsBuiltin),
                                 list(worker.declaredArgumentsAsBuiltin))
            elif name == 'A5':
                results[name] = (bool(worker.unusedImports), worker.unusedImports)
            else:
                results[name] = getattr(worker, attr)
        return results

    @staticmethod
    def _run_stateless(method_name, root, *args):
        worker = VisitorMC3()
        getattr(worker, method_name)(root, *args)
        return worker

    def getA2(self, root):
        return self._run_stateless('checkSelfAssignment', root).selfAssignment

    def getA3(self, root):
        return self._run_stateless('checkUnusedInitVariables', root).unusedInitVar

    def getA4(self, root):
        worker = self._run_stateless('checkBuiltInRedefinition', root)
        return (worker.builtinRedefinition, list(worker.declaredVariablesAsBuiltIn),
                list(worker.declaredFunctionsAsBuiltin), list(worker.declaredArgumentsAsBuiltin))

    def getA5(self, root):
        worker = self._run_stateless('checkUnusedImports', root)
        return len(worker.unusedImports) > 0, worker.unusedImports

    def getB4(self, root):
        return self._run_stateless('checkRepeatedCommandsInIfs', root).repeatedCommandsInIfs

    def getB6(self, root):
        return self._run_stateless('checkBooleanAttemptedWithWhile', root).boolOpAttemptedWithWhile

    def getB8(self, root):
        return self._run_stateless('checkNonUtilizationElifElse', root).nonUtilizationElifElse

    def getB9(self, root):
        return self._run_stateless('checkElifRetestingCondition', root).elifRetestingCondition

    def getB10(self, root):
        return self._run_stateless('checkUnnecessaryElifElse', root).unnecessaryElifElse

    def getB11(self, root):
        return self._run_stateless('checkIfsWithSameBody', root).sameBodyIfs

    def getB12(self, root):
        return self._run_stateless('checkConsecutiveIfs', root).consecutiveEqualIfs

    def getC1(self, root):
        return self._run_stateless('checkWhileCondInItsBody', root).whileCondInItsBody

    def getC2(self, root):
        return self._run_stateless('checkRedundantLoop', root).redundantLoop

    def getC3(self, root):
        return self._run_stateless('checkRedundantOpsInLoop', root).redundantOpsInLoop

    def getC4(self, root, config=None):
        if isinstance(config, int):
            config = MC3Config(c4_range_threshold=config)
        config = config or MC3Config()
        return self._run_stateless('checkForWithConstant', root, config.c4_range_threshold).forWithConstant

    def getC8(self, root):
        return self._run_stateless('checkForOverwritten', root, []).forVariableOverwritten

    def getD4(self, root):
        return self._run_stateless('checkVarOutsideFuncScope', root).varOutsideFuncScope

    def getE1(self, root):
        return self._run_stateless('checkAllCombinationsRedundancy', root).excessiveCombinationChecks

    def getE2(self, root, config=None):
        if isinstance(config, int):
            config = MC3Config(e2_list_threshold=config)
        config = config or MC3Config()
        return self._run_stateless('checkListOverusage', root, config.e2_list_threshold).listOverusage

    def getG4(self, root, config=None, func_len=None, total=None):
        if isinstance(config, int):
            config = MC3Config(g4_min_var_chars=config,
                               g4_min_func_chars=(func_len if func_len is not None else 8),
                               g4_max_nonsignificant_percent=(total if total is not None else 70))
        config = config or MC3Config()
        return self._run_stateless('checkNonSignificantNames', root, config.g4_min_var_chars,
                                   config.g4_min_func_chars, config.g4_max_nonsignificant_percent).nonSignificantNames

    def getG5(self, root):
        return self._run_stateless('checkArbitraryDeclarations', root).arbitraryDeclarations

    def getH1(self, root):
        return self._run_stateless('checkNoEffectStatement', root).noEffectStatement
