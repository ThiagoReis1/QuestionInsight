"""
VisitorMC3 - Detector de Misconceptions (MC³) em Código Python
===============================================================

CORREÇÕES APLICADAS (v7 → v8):
    ✅ C4:  Correção de step negativo em range(N, 0, -step).

        PROBLEMA — UnaryOp para literais negativos:
            for i in range(100, 0, -1):
                pass
            O parser do Python representa o literal -1 como
            UnaryOp(op=USub(), operand=Constant(value=1))
            e NÃO como Constant(value=-1).
            A versão anterior verificava apenas isinstance(step, ast.Constant),
            nunca batia para -1 escrito diretamente, e portanto range(N,0,-1)
            não era detectado como loop grande mesmo com N >= threshold.

            CORREÇÃO: resolve step_val considerando os dois casos:
                • Constant(value=v)            → step_val = v
                • UnaryOp(USub, Constant(v))   → step_val = -v
            Se step_val < 0, usa args[0] como limite; senão, args[1].

CORREÇÕES ANTERIORES (v6 → v7) mantidas:
    ✅ A3:  Reescrita completa de checkUnusedInitVariables.

        PROBLEMA 1 — Falso positivo em if/else bifurcado:
            def foo():
                if cond:
                    x = 0    ← branch A
                else:
                    x = 1    ← branch B
                return x     ← x é usado: sem misconception
            _walk_ordered_stmts descia linearmente nos dois branches,
            fazendo x entrar em pending_write duas vezes. Na segunda
            atribuição, x já estava em pending_write → falso "escrita morta".

            CORREÇÃO: pending_write agora usa um set por branch. Ao sair
            de um nó composto (If/For/While/Try), os conjuntos de todos os
            branches são INTERSECTADOS: só permanece em pending_write o que
            estava pendente em TODOS os caminhos (ou seja, nunca foi lido
            em nenhum deles). Atribuições que existem em apenas um branch
            não são consideradas "mortas".

        PROBLEMA 2 — Escopo global sem pending_write:
            x = 1
            x = 2   ← escrita morta, não detectada
            print(x)
            A análise global usava apenas declared/used sem rastrear
            sequência. Agora aplica a mesma lógica de pending_write
            do escopo de funções também ao escopo global (top-level),
            usando _analyze_stmts() unificada.

        PROBLEMA 3 — global_used capturava nomes dentro de funções:
            x = 10          ← global
            def foo():
                print(x)    ← uso via escopo externo (MC D4)
            ast.walk(root) entrava na função e adicionava x a global_used,
            mascarando a variável global não utilizada no escopo global.
            CORREÇÃO: global_used agora é coletado apenas fora de funções.

CORREÇÕES ANTERIORES (v5 → v6) mantidas:
    ✅ A3:  _walk_ordered_stmts() substitui ast.walk para ordem de execução
    ✅ B6:  Lógica de break unificada (direto / em if / em loop interno)
    ✅ D4:  getLocalVars usa ast.walk sobre todo o corpo da função

CORREÇÕES ANTERIORES (v4 → v5) mantidas:
    ✅ C4:  range(N, 0, -step) usa args[0] quando step negativo
    ✅ G5:  async def após código executável é detectado
    ✅ D4b: AugAssign target detecta acesso a global
    ✅ A3c: Primeira atribuição morta detectada em funções
    ✅ G4:  Nome convencional '_' excluído da verificação
"""

import ast


# =============================================================================
# CLASSE AUXILIAR
# =============================================================================

class VisitorMC3Helper:

    @staticmethod
    def compare_ast_nodes(node1, node2):
        if isinstance(node1, ast.Name) and isinstance(node2, ast.Name):
            return node1.id == node2.id
        if isinstance(node1, ast.Constant) and isinstance(node2, ast.Constant):
            return node1.value == node2.value
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

    def reset(self):
        self.__init__()

    # =========================================================================
    # UTILITÁRIO INTERNO — TRAVESSIA ORDENADA
    # =========================================================================

    @staticmethod
    def _walk_ordered_stmts(stmts):
        """
        Gerador que percorre uma lista de statements em ordem de execução,
        descendo recursivamente nos blocos compostos (if/elif/else, for,
        while, with, try/except/finally).

        NÃO desce em FunctionDef/AsyncFunctionDef aninhadas para não
        misturar escopos.
        """
        for stmt in stmts:
            yield stmt
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue   # escopo separado — não desce
            for child_list in VisitorMC3._get_child_stmt_lists(stmt):
                yield from VisitorMC3._walk_ordered_stmts(child_list)

    @staticmethod
    def _get_child_stmt_lists(node):
        """
        Retorna listas de statements filho de um nó composto, na ordem
        lógica de execução:
            if/for/while : body, orelse
            with         : body
            try          : body, handlers[*].body, orelse, finalbody
        """
        if isinstance(node, (ast.If, ast.For, ast.While)):
            yield node.body
            if node.orelse:
                yield node.orelse
        elif isinstance(node, ast.With):
            yield node.body
        elif isinstance(node, ast.Try):
            yield node.body
            for handler in node.handlers:
                yield handler.body
            if node.orelse:
                yield node.orelse
            if node.finalbody:
                yield node.finalbody

    # =========================================================================
    # CATEGORIA A
    # =========================================================================

    def checkSelfAssignment(self, root):
        """A2 — Variável atribuída a si mesma (ex: x = x)."""
        self.selfAssignment = False
        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and isinstance(node.value, ast.Name):
                        if target.id == node.value.id:
                            self.selfAssignment = True
                            return

    # -------------------------------------------------------------------------
    # A3 — REESCRITA COMPLETA (v7)
    # -------------------------------------------------------------------------

    def checkUnusedInitVariables(self, root):
        """
        A3 — Variável inicializada mas nunca utilizada / escrita morta.

        CORREÇÃO A3 (v7): análise sensível a fluxo com pending_write por branch.

        Estratégia central — _analyze_stmts(stmts, used, pending):
          • Percorre statements em ordem de execução.
          • pending  : set de variáveis escritas mas ainda não lidas.
          • used     : set acumulado de variáveis já lidas em algum ponto.

          Nós compostos (If/For/While/Try) são tratados com análise por branch:
            1. Cada branch recebe uma CÓPIA de pending.
            2. Cada branch é analisado independentemente.
            3. Ao final, pending ← INTERSECÇÃO dos pending de todos os branches.
               Isso garante: só fica em pending o que está pendente em TODOS os
               caminhos, ou seja, nunca foi lido em nenhum deles.

          Consequência: atribuição em apenas um branch de if/else NÃO é
          considerada escrita morta, eliminando o falso positivo da v6.

        Escopo global:
          • Aplica a mesma lógica de pending_write (correção do Problema 2).
          • global_used coletado apenas fora de funções (correção do Problema 3).
        """
        self.unusedInitVar = False

        # ------------------------------------------------------------------
        # Núcleo: analisa uma lista de statements, atualizando used/pending.
        # Retorna True se uma misconception foi encontrada.
        # ------------------------------------------------------------------
        def _collect_reads(node, used, pending):
            """
            Registra todas as leituras de Name em node.
            NÃO desce em FunctionDef/AsyncFunctionDef aninhadas para não
            misturar escopos: uso de 'x' dentro de uma função não conta
            como leitura de 'x' no escopo externo.
            """
            queue = list(ast.iter_child_nodes(node))
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used.add(node.id)
                pending.discard(node.id)
            while queue:
                n = queue.pop()
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue   # barreira de escopo — não desce
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                    used.add(n.id)
                    pending.discard(n.id)
                queue.extend(ast.iter_child_nodes(n))

        def _analyze_stmts(stmts, used, pending, is_function_scope=False):
            """
            Analisa stmts em sequência.
            Retorna True se misconception detectada, False caso contrário.
            Modifica used e pending in-place.
            """
            for stmt in stmts:

                # -- Assign: lê RHS, depois escreve targets --
                if isinstance(stmt, ast.Assign):
                    # 1. Leituras no lado direito
                    _collect_reads(stmt.value, used, pending)
                    # 2. Cada target
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            var = target.id
                            if var in pending:
                                # escrita sobre escrita sem leitura → morta
                                return True
                            if var not in used:
                                pending.add(var)
                        elif isinstance(target, (ast.Tuple, ast.List)):
                            for elt in target.elts:
                                if isinstance(elt, ast.Name):
                                    var = elt.id
                                    if var in pending:
                                        return True
                                    if var not in used:
                                        pending.add(var)
                        else:
                            # atribuição a atributo/subscript: lê o alvo
                            _collect_reads(target, used, pending)

                # -- AugAssign: lê e escreve (x += 1 implica leitura de x) --
                elif isinstance(stmt, ast.AugAssign):
                    if isinstance(stmt.target, ast.Name):
                        used.add(stmt.target.id)
                        pending.discard(stmt.target.id)
                    _collect_reads(stmt.value, used, pending)

                # -- Return: registra leituras --
                elif isinstance(stmt, ast.Return):
                    if stmt.value is not None:
                        _collect_reads(stmt.value, used, pending)

                # -- FunctionDef/AsyncFunctionDef aninhada: não desce --
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    pass  # escopo separado, analisado depois

                # -- If: analisa condição + branches independentes --
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

                # -- For: analisa iter + body + orelse independentes --
                elif isinstance(stmt, ast.For):
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

                # -- While: analisa condição + body + orelse --
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

                # -- Try: trata cada bloco como branch independente --
                elif isinstance(stmt, ast.Try):
                    branches = [stmt.body]
                    for handler in stmt.handlers:
                        branches.append(handler.body)
                    if stmt.orelse:
                        branches.append(stmt.orelse)
                    # finalbody sempre executa — processa em sequência depois
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

                # -- With: analisa context managers + body --
                elif isinstance(stmt, ast.With):
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

                # -- Qualquer outro stmt: apenas registra leituras --
                else:
                    _collect_reads(stmt, used, pending)

            return False

        # ------------------------------------------------------------------
        # Escopo global (top-level)
        # ------------------------------------------------------------------

        # 1. Todas as leituras no arquivo inteiro (incluindo funções)
        all_file_reads = set()
        for n in ast.walk(root):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                all_file_reads.add(n.id)

        # 2. Statements top-level (sem FunctionDef/AsyncFunctionDef)
        global_stmts = [
            node for node in ast.iter_child_nodes(root)
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        # A) Detecção de escrita morta — used começa vazio
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

        # ------------------------------------------------------------------
        # Escopos de funções
        # ------------------------------------------------------------------
        for node in ast.walk(root):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue

            func_used    = set()
            func_pending = set()

            # Parâmetros já são "conhecidos" — não são escritas pendentes
            for arg in node.args.args:
                func_used.add(arg.arg)

            if _analyze_stmts(node.body, func_used, func_pending,
                               is_function_scope=True):
                self.unusedInitVar = True
                return

            # Variáveis declaradas na função mas nunca lidas
            if func_pending:
                self.unusedInitVar = True
                return

    def checkBuiltInRedefinition(self, root):
        """A4 — Redefinição de função/variável built-in do Python."""
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
        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name) and tgt.id in list_of_builtins:
                        self.declaredVariablesAsBuiltIn.add(tgt.id)
                    if isinstance(tgt, ast.Tuple):
                        for name in tgt.elts:
                            if isinstance(name, ast.Name) and name.id in list_of_builtins:
                                self.declaredVariablesAsBuiltIn.add(name.id)
            elif isinstance(node, ast.FunctionDef):
                if node.name in list_of_builtins:
                    self.declaredFunctionsAsBuiltin.add(node.name)
                for arg in node.args.args:
                    if arg.arg in list_of_builtins:
                        self.declaredArgumentsAsBuiltin.add(arg.arg)

        if (len(self.declaredVariablesAsBuiltIn) +
                len(self.declaredFunctionsAsBuiltin) +
                len(self.declaredArgumentsAsBuiltin) > 0):
            self.builtinRedefinition = True

    def checkUnusedImports(self, root):
        """A5 — Importação não utilizada. Ignora 'from X import *'."""
        import_names = set()
        used_names   = set()

        for node in ast.walk(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_names.add(alias.asname or alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == '*':
                        continue
                    import_names.add(alias.asname or alias.name)

        for node in ast.walk(root):
            if isinstance(node, ast.Name):
                used_names.add(node.id)

        self.unusedImports = list(import_names - used_names)

    # =========================================================================
    # CATEGORIA B
    # =========================================================================

    def checkRepeatedCommandsInIfs(self, root):
        """B4 — Comandos repetidos dentro de blocos if/elif/else."""
        def check_if_chain(node):
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
            block_sources = ["|".join([ast.dump(s) for s in body]) for body in blocks]
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
        """
        B6 — Tentativa de usar while como if com condição booleana.

        CORREÇÃO B6 (v6) mantida: lógica de break unificada em única passagem.
          - break direto no body           → has_direct_break = True
          - break dentro de if sem loop    → has_if_break = True
          - qualquer outro stmt com lógica → has_real_work = True
        """
        def _has_break_no_loop(node):
            """True se houver Break acessível sem cruzar For/While interno."""
            if isinstance(node, ast.Break):
                return True
            if isinstance(node, (ast.For, ast.While)):
                return False
            return any(_has_break_no_loop(c) for c in ast.iter_child_nodes(node))

        for node in ast.walk(root):
            if not isinstance(node, ast.While):
                continue
            if not isinstance(node.test, (ast.Compare, ast.BoolOp)):
                continue

            has_direct_break = False
            has_if_break     = False
            has_real_work    = False

            for stmt in node.body:
                if isinstance(stmt, ast.Break):
                    has_direct_break = True
                    continue

                if isinstance(stmt, ast.If):
                    if _has_break_no_loop(stmt):
                        orelse_has_work = any(
                            not isinstance(s, ast.Pass) for s in stmt.orelse
                        )
                        if not orelse_has_work:
                            has_if_break = True
                            continue
                    has_real_work = True
                    continue

                has_real_work = True

            if (has_direct_break or has_if_break) and not has_real_work:
                self.boolOpAttemptedWithWhile = True
                return

    def checkNonUtilizationElifElse(self, root):
        """B8 — Cadeia if/elif sem else final."""
        self.nonUtilizationElifElse = False
        for node in ast.walk(root):
            if isinstance(node, ast.If):
                if not node.orelse:
                    continue
                if not isinstance(node.orelse[0], ast.If):
                    continue
                current = node.orelse[0]
                while isinstance(current, ast.If):
                    if not current.orelse:
                        self.nonUtilizationElifElse = True
                        return
                    if not isinstance(current.orelse[0], ast.If):
                        break
                    current = current.orelse[0]

    def checkElifRetestingCondition(self, root):
        """B9 — elif retestando condição inversa do if anterior."""
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

        for node in ast.walk(root):
            if isinstance(node, ast.If):
                if len(node.orelse) > 0 and isinstance(node.test, ast.Compare):
                    for chd in node.orelse:
                        if isinstance(chd, ast.If):
                            compareElifsR(chd.test, node.test.left,
                                          node.test.ops, node.test.comparators)

    def checkUnnecessaryElifElse(self, root):
        """B10 — elif/else desnecessário após bloco if vazio ou com apenas pass."""
        def is_empty_or_pass_only(body):
            if not body:
                return True
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                return True
            return False

        for node in ast.walk(root):
            if isinstance(node, ast.If):
                if is_empty_or_pass_only(node.body) and node.orelse:
                    self.unnecessaryElifElse = True
                    return
                if node.orelse and isinstance(node.orelse[0], ast.If):
                    if is_empty_or_pass_only(node.orelse[0].body):
                        self.unnecessaryElifElse = True
                        return

    def checkIfsWithSameBody(self, root):
        """B11 — Ifs distintos com blocos de código idênticos."""
        self.sameBodyIfs = False

        def check_scope(node):
            seen_bodies = {}
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If):
                    body_repr = "|".join([ast.dump(s) for s in child.body])
                    if body_repr in seen_bodies:
                        self.sameBodyIfs = True
                        return
                    seen_bodies[body_repr] = True
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef,
                                      ast.For, ast.While, ast.With,
                                      ast.If, ast.Try)):
                    check_scope(child)
                    if self.sameBodyIfs:
                        return

        check_scope(root)

    def checkConsecutiveIfs(self, root):
        """B12 — Ifs consecutivos com a mesma condição mas ações distintas."""
        for node in ast.walk(root):
            conseqIf = False
            firstIf  = None
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If) and not conseqIf:
                    if len(child.orelse) == 0:
                        conseqIf = True
                        firstIf  = child
                elif isinstance(child, ast.If) and conseqIf:
                    if len(child.orelse) == 0:
                        secondIf = child
                        if (isinstance(firstIf.test, ast.Name) and
                                isinstance(secondIf.test, ast.Name)):
                            if firstIf.test.id == secondIf.test.id:
                                self.consecutiveEqualIfs = True
                                return
                        if (isinstance(firstIf.test, ast.Compare) and
                                isinstance(secondIf.test, ast.Compare)):
                            L = VisitorMC3Helper.compare_ast_nodes(
                                firstIf.test.left, secondIf.test.left)
                            O = VisitorMC3Helper.compare_ops_equal(
                                firstIf.test.ops, secondIf.test.ops)
                            R = VisitorMC3Helper.compare_comparators(
                                firstIf.test.comparators, secondIf.test.comparators)
                            if L and O and R:
                                self.consecutiveEqualIfs = True
                                return
                    conseqIf = False
                else:
                    conseqIf = False

    # =========================================================================
    # CATEGORIA C
    # =========================================================================

    def checkWhileCondInItsBody(self, root):
        """C1 — Condição do while retestada dentro do próprio corpo."""
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Compare):
                    for item in node.body:
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
        """C2 — Loop redundante (executa exatamente uma vez)."""
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Constant) and node.test.value is True:
                    for item in node.body:
                        if isinstance(item, ast.Break):
                            self.redundantLoop = True
                            return
        for node in ast.walk(root):
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
        """C3 — Operações idênticas repetidas dentro do loop."""
        for node in ast.walk(root):
            if isinstance(node, (ast.For, ast.While)):
                seen = set()
                for stmt in node.body:
                    if isinstance(stmt, (ast.Assign, ast.Expr)):
                        code_repr = ast.dump(stmt)
                        if code_repr in seen:
                            self.redundantOpsInLoop = True
                            return
                        seen.add(code_repr)

    def checkForWithConstant(self, root, constThreshold=50):
        """
        C4 — for com número fixo e grande de iterações (deveria ser while).

        CORREÇÃO C4 (v8): step negativo escrito como literal (ex: -1) é
        representado pelo parser como UnaryOp(USub, Constant(1)), não como
        Constant(-1). A versão anterior só verificava Constant, portanto
        range(N, 0, -1) nunca era detectado. Agora resolve step_val
        para os dois casos antes de decidir qual argumento é o limite.
        """
        for node in ast.walk(root):
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
        """C8 — Variável de iteração do for sobrescrita dentro do loop."""
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

        for node in ast.walk(root):
            if isinstance(node, ast.For):
                varIter       = getVarIter(node)
                all_iter_vars = prevIterVars + varIter
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Name):
                                if target.id in all_iter_vars:
                                    self.forVariableOverwritten = True
                                    return
                            elif isinstance(target, ast.Tuple):
                                for elem in target.elts:
                                    if isinstance(elem, ast.Name):
                                        if elem.id in all_iter_vars:
                                            self.forVariableOverwritten = True
                                            return
                    elif isinstance(stmt, ast.AugAssign):
                        if isinstance(stmt.target, ast.Name):
                            if stmt.target.id in all_iter_vars:
                                self.forVariableOverwritten = True
                                return
                    elif isinstance(stmt, ast.For):
                        self.checkForOverwritten(stmt, all_iter_vars)
                        if self.forVariableOverwritten:
                            return

    # =========================================================================
    # CATEGORIA D
    # =========================================================================

    def checkVarOutsideFuncScope(self, root):
        """
        D4 — Função acessando variáveis do escopo externo (global).

        CORREÇÃO D4 (v6) mantida: getLocalVars usa ast.walk sobre todo o
        corpo da função, capturando atribuições em qualquer profundidade.
        Correção D4b (v5) mantida: AugAssign detecta acesso a global.
        """
        def getGlobalVars(root):
            globalVars = set()
            for node in ast.iter_child_nodes(root):
                if not isinstance(node, ast.FunctionDef):
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
            for arg in funcNode.args.args:
                localVars.add(arg.arg)
            for node in ast.walk(funcNode):
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
            return localVars

        def checkNameUsage(nameNode, localVars, globalVars):
            if isinstance(nameNode, ast.Name):
                if nameNode.id in globalVars and nameNode.id not in localVars:
                    self.varOutsideFuncScope = True
                    return True
            return False

        def checkVarUsage(stm, localVars, globalVars):
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
            if isinstance(stm, ast.Assign):
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.AugAssign):
                if checkNameUsage(stm.target, localVars, globalVars): return
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, (ast.If, ast.While)):
                for node in ast.walk(stm.test):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.For):
                for node in ast.walk(stm.iter):
                    if checkNameUsage(node, localVars, globalVars): return
            if isinstance(stm, ast.Return) and stm.value is not None:
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars): return

        globalVars = getGlobalVars(root)
        for node in ast.walk(root):
            if isinstance(node, ast.FunctionDef):
                localVars = getLocalVars(node)
                for item in node.body:
                    for stm in ast.walk(item):
                        checkVarUsage(stm, localVars, globalVars)
                        if self.varOutsideFuncScope:
                            return

    # =========================================================================
    # CATEGORIA E
    # =========================================================================

    def checkAllCombinationsRedundancy(self, root):
        """E1 — Verificação excessiva de combinações (>5 condições em um if)."""
        self.excessiveCombinationChecks = False
        for node in ast.walk(root):
            if isinstance(node, ast.If) and isinstance(node.test, ast.BoolOp):
                if isinstance(node.test.op, (ast.And, ast.Or)):
                    if len(node.test.values) > 5:
                        self.excessiveCombinationChecks = True
                        return

    def checkListOverusage(self, root, numListThreshold=5):
        """E2 — Uso excessivo de listas (>= threshold listas declaradas)."""
        numLists = 0
        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                if isinstance(node.value, (ast.List, ast.ListComp)):
                    numLists += 1
        if numLists >= numListThreshold:
            self.listOverusage = True

    # =========================================================================
    # CATEGORIA G
    # =========================================================================

    def checkNonSignificantNames(self, root, varLenThreshold, funcLenThreshold,
                                  totalNamesThreshold):
        """
        G4 — Variáveis/funções com nomes não significativos (muito curtos).
        Correção G4c (v5) mantida: '_' excluído como convenção de descarte.
        """
        EXCLUDED_PARAMS = {'self', 'cls'}
        EXCLUDED_VARS   = {'_'}

        def collectVariableNames(root):
            names = []
            for node in ast.walk(root):
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

        def collectFunctionNames(root):
            names = []
            for node in ast.walk(root):
                if isinstance(node, ast.FunctionDef):
                    if node.name not in names:
                        names.append(node.name)
            return names

        def collectParamNames(root):
            names = []
            for node in ast.walk(root):
                if isinstance(node, ast.FunctionDef):
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
        """
        G5 — Funções declaradas após código executável.
        Correção G5b (v5) mantida: AsyncFunctionDef tratado igual a FunctionDef.
        """
        self.arbitraryDeclarations = False
        found_executable_code = False

        for node in ast.iter_child_nodes(root):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                continue
            if VisitorMC3Helper.is_block_comment(node):
                continue
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if found_executable_code:
                    self.arbitraryDeclarations = True
                    return
            else:
                found_executable_code = True

    # =========================================================================
    # CATEGORIA H
    # =========================================================================

    def checkNoEffectStatement(self, root):
        """H1 — Statement sem efeito (literal numérico/booleano/None solto)."""
        for node in ast.walk(root):
            if isinstance(node, ast.Expr):
                if isinstance(node.value, ast.Constant):
                    if not isinstance(node.value.value, str):
                        self.noEffectStatement = True
                        return

    # =========================================================================
    # INTERFACE PÚBLICA — MÉTODOS GET
    # =========================================================================

    def getA2(self, root):
        self.selfAssignment = False
        self.checkSelfAssignment(root)
        return self.selfAssignment

    def getA3(self, root):
        self.unusedInitVar = False
        self.checkUnusedInitVariables(root)
        return self.unusedInitVar

    def getA4(self, root):
        self.builtinRedefinition = False
        self.declaredVariablesAsBuiltIn = set()
        self.declaredFunctionsAsBuiltin = set()
        self.declaredArgumentsAsBuiltin = set()
        self.checkBuiltInRedefinition(root)
        return (self.builtinRedefinition,
                list(self.declaredVariablesAsBuiltIn),
                list(self.declaredFunctionsAsBuiltin),
                list(self.declaredArgumentsAsBuiltin))

    def getA5(self, root):
        self.unusedImports = []
        self.checkUnusedImports(root)
        return len(self.unusedImports) > 0, self.unusedImports

    def getB4(self, root):
        self.repeatedCommandsInIfs = False
        self.checkRepeatedCommandsInIfs(root)
        return self.repeatedCommandsInIfs

    def getB6(self, root):
        self.boolOpAttemptedWithWhile = False
        self.checkBooleanAttemptedWithWhile(root)
        return self.boolOpAttemptedWithWhile

    def getB8(self, root):
        self.nonUtilizationElifElse = False
        self.checkNonUtilizationElifElse(root)
        return self.nonUtilizationElifElse

    def getB9(self, root):
        self.elifRetestingCondition = False
        self.checkElifRetestingCondition(root)
        return self.elifRetestingCondition

    def getB10(self, root):
        self.unnecessaryElifElse = False
        self.checkUnnecessaryElifElse(root)
        return self.unnecessaryElifElse

    def getB11(self, root):
        self.sameBodyIfs = False
        self.checkIfsWithSameBody(root)
        return self.sameBodyIfs

    def getB12(self, root):
        self.consecutiveEqualIfs = False
        self.checkConsecutiveIfs(root)
        return self.consecutiveEqualIfs

    def getC1(self, root):
        self.whileCondInItsBody = False
        self.checkWhileCondInItsBody(root)
        return self.whileCondInItsBody

    def getC2(self, root):
        self.redundantLoop = False
        self.checkRedundantLoop(root)
        return self.redundantLoop

    def getC3(self, root):
        self.redundantOpsInLoop = False
        self.checkRedundantOpsInLoop(root)
        return self.redundantOpsInLoop

    def getC4(self, root, constThreshold=50):
        self.forWithConstant = False
        self.checkForWithConstant(root, constThreshold)
        return self.forWithConstant

    def getC8(self, root):
        self.forVariableOverwritten = False
        self.checkForOverwritten(root, [])
        return self.forVariableOverwritten

    def getD4(self, root):
        self.varOutsideFuncScope = False
        self.checkVarOutsideFuncScope(root)
        return self.varOutsideFuncScope

    def getE1(self, root):
        self.excessiveCombinationChecks = False
        self.checkAllCombinationsRedundancy(root)
        return self.excessiveCombinationChecks

    def getE2(self, root, numListsThreshold=5):
        self.listOverusage = False
        self.checkListOverusage(root, numListsThreshold)
        return self.listOverusage

    def getG4(self, root, varLenThreshold, funcLenThreshold, totalNamesThreshold):
        self.nonSignificantNames = False
        self.checkNonSignificantNames(root, varLenThreshold, funcLenThreshold,
                                       totalNamesThreshold)
        return self.nonSignificantNames

    def getG5(self, root):
        self.arbitraryDeclarations = False
        self.checkArbitraryDeclarations(root)
        return self.arbitraryDeclarations

    def getH1(self, root):
        self.noEffectStatement = False
        self.checkNoEffectStatement(root)
        return self.noEffectStatement