"""
VisitorMC3 - Detector de Misconceptions (MC³) em Código Python
===============================================================

CORREÇÕES APLICADAS (v10 → v11):
    ✅ A2:  same_reference agora reconhece atribuição múltipla via
            tupla/lista (`x, y = x, y`), não só Name/Attribute/Subscript
            isolados — trocas reais (`x, y = y, x`) continuam sem disparo.
    ✅ A4:  ast.AsyncFor/ast.AsyncWith agora contam como declaração de
            variável ao sombrear um builtin (`async for list in ...:`,
            `async with x() as str:`), igual a For/With.
    ✅ A3:  ast.AsyncFor/ast.AsyncWith agora recebem a mesma análise de
            escrita morta (pending) que For/With — antes caíam num ramo
            genérico que só registrava leituras, nunca sinalizando
            variável nunca usada dentro desses blocos.
    ✅ C3:  ast.AsyncFor agora inicia a checagem de operações duplicadas
            (antes só For/While), e o helper de descida em blocos
            aninhados (_get_child_stmt_lists) passa a reconhecer também
            AsyncFor/AsyncWith aninhados dentro de qualquer loop.

CORREÇÕES ANTERIORES (v9 → v10) mantidas:
    ✅ B4:  Ramos triviais (pass/return/raise/continue/break) repetidos
            numa cadeia if/elif/else não contam mais como duplicação
            (mesmo idioma de guard clause que B11 já excluía).
    ✅ B11: ast.AsyncFor e ast.AsyncWith agora entram na recursão —
            ifs duplicados dentro de `async for`/`async with` detectados.
    ✅ E1:  Padrão (b) agora reconhece negação por operador de comparação
            invertido (`idade < 18` como negação de `idade >= 18`), não
            só `not` explícito — a forma mais comum na prática da
            misconception "if/elif enumerando todas as combinações".
    ✅ E2:  ast.AnnAssign (`x: list = []`) agora conta para o total de
            listas declaradas, não só ast.Assign.
    ✅ G4:  ast.AsyncFunctionDef tratado igual a ast.FunctionDef na
            coleta de nomes de função e de parâmetro.

CORREÇÕES ANTERIORES (v8 → v9) mantidas:
    ✅ B6:  while com condição booleana solta (variável ou `not variável`)
            agora é detectado, não só while com Compare/BoolOp.
    ✅ G5:  ast.ClassDef antes de uma função não conta mais como "código
            executável" (falso positivo removido).
    ✅ H1:  ast.UnaryOp solto (`not flag`, `-x` sem uso) agora conta como
            statement sem efeito.
    ✅ C8:  ast.AsyncFor tratado como ast.For (variável de iteração de
            `async for` sobrescrita no corpo agora é detectada).
    ✅ D4:  ast.AsyncFor também verificado em checkVarUsage (leitura de
            global no `.iter` de um `async for` agora é detectada).

CORREÇÕES ANTERIORES (v7 → v8) mantidas:
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
        """
        CORREÇÃO (v9): antes só reconhecia ast.Name e ast.Constant — uma
        chamada de método (ex: contador.valor()) nos dois lados nunca era
        considerada igual, mesmo sendo a mesma expressão. Adicionado um
        fallback estrutural genérico (mesmo tipo de nó + mesmo ast.dump)
        que cobre Call, Attribute, BinOp etc. sem afetar os casos já
        tratados explicitamente acima.
        """
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

        CORREÇÃO (v18): ast.AsyncFor e ast.AsyncWith não eram reconhecidos
        aqui (só as variantes síncronas), então qualquer checagem que
        reaproveita este helper para descer em blocos aninhados (C1, C3,
        C8) parava de enxergar o que houvesse dentro de um `async for`/
        `async with` aninhado. Agora tratadas como For/With.
        """
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
        """
        True se a sequência de statements garante break em TODO
        caminho de execução (não apenas se existe algum break
        solto em algum lugar). Considera: break direto, ou um if
        aninhado cujos dois ramos (if e else) garantam break.
        Não atravessa For/While internos.

        Extraído (v13) de checkBooleanAttemptedWithWhile (B6) para ser
        reaproveitado também por checkRedundantLoop (C2) — ambos precisam
        da mesma noção de "break garantido em todo caminho", incluindo
        quando o break está dentro de um if aninhado.
        """
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
        """
        True somente se TODOS os caminhos do if garantem break:
        o ramo 'if' quebra E o ramo 'else' também quebra.
        Um else vazio, com só 'pass', ou inexistente NÃO conta
        como caminho que quebra -- ali o loop apenas continua.
        """
        if_branch_breaks = VisitorMC3._has_break_no_loop_all(if_node.body)
        if not if_node.orelse:
            return False
        else_branch_breaks = VisitorMC3._has_break_no_loop_all(if_node.orelse)
        return if_branch_breaks and else_branch_breaks

    # =========================================================================
    # CATEGORIA A
    # =========================================================================

    def checkSelfAssignment(self, root):
        """
        A2 — Variável ou atributo atribuído a si mesmo (ex: x = x, self.a = self.a).

        CORREÇÃO (v11): a versão anterior só reconhecia Name = Name (x = x).
        A mesma besteira via atributo de instância (self.saldo = self.saldo)
        passava batido porque o alvo e o valor são ast.Attribute, não
        ast.Name. Agora compara estruturalmente os dois lados, cobrindo
        também cadeias de atributo (self.a.b = self.a.b).

        CORREÇÃO (v12): same_reference não reconhecia ast.Subscript. O
        mesmo erro via indexação (lista[0] = lista[0], dados["x"] = dados["x"])
        caía no 'return False' final e nunca era detectado, mesmo sendo
        estruturalmente idêntico ao caso Name/Attribute já tratado. Agora
        Subscript compara recursivamente a base (.value) e o índice (.slice),
        reaproveitando VisitorMC3Helper.compare_ast_nodes para o índice.

        CORREÇÃO (v18): same_reference também não reconhecia atribuição
        múltipla via tupla/lista (`x, y = x, y`) -- um alvo ast.Tuple/
        ast.List caía direto no 'return False' final, mesmo quando CADA
        elemento, em ordem, é uma auto-atribuição. Isso é a mesma
        misconception (nada muda), só que com mais de uma variável de
        uma vez. Agora Tuple/List compara elemento a elemento,
        recursivamente -- então `x, y = y, x` (troca real de valores,
        idioma válido) continua NÃO sendo marcado, só a cópia exata.
        """
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

        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if same_reference(target, node.value):
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

            CORREÇÃO (v13): lambdas e comprehensions (list/set/dict/
            generator) têm escopo próprio para os nomes que vinculam
            (parâmetros da lambda, variável de 'for' da comprehension).
            A versão anterior tratava QUALQUER Name com ctx=Load como
            leitura da variável externa de mesmo nome, mesmo quando esse
            nome era, na verdade, sombreado por um parâmetro de lambda
            ou pela variável de uma comprehension -- mascarando uma
            escrita morta de verdade. Ex.:
                x = 5
                f = lambda x: x + 1   # x externo nunca é lido de fato
            ou
                x = 5
                return [x for x in range(10)]  # idem
            Agora rastreamos os nomes sombreados em cada escopo aninhado
            e ignoramos leituras desses nomes enquanto sombreados.
            """
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
                    return  # barreira de escopo completa — não desce
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
            """
            Retorna o conjunto de nomes lidos (ast.Load) dentro de
            funcnode (incluindo funções aninhadas mais profundas) que
            NÃO são atribuídos/parâmetros em nenhum nível dessa árvore
            -- ou seja, variáveis livres que só podem ter vindo de um
            escopo externo (closure). Uma aproximação estática simples:
            não modela 'nonlocal'/'global' explicitamente, mas cobre o
            caso comum de uma função aninhada apenas lendo uma variável
            do escopo que a envolve.
            """
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
            """
            Analisa stmts em sequência.
            Retorna True se misconception detectada, False caso contrário.
            Modifica used e pending in-place.

            CORREÇÃO (v11): 'pending_at_entry' guarda uma foto do que já
            estava pendente ANTES desta lista de statements começar a ser
            processada. Isso distingue dois casos que antes eram tratados
            igual:
              1) Uma variável é escrita, e SEM SAIR do bloco atual, é
                 sobrescrita de novo sem nunca ter sido lida -- isso É
                 escrita morta de verdade (var entra em pending DURANTE
                 esta mesma chamada, então não está em pending_at_entry).
              2) Uma variável já estava pendente ANTES de entrar num branch
                 condicional (if/elif/else, while, for, try), e esse branch
                 específico a sobrescreve sem ler -- isso NÃO é
                 necessariamente morta, porque outro branch (ou o código
                 após o if) ainda pode ler o valor original. Ex.: valor
                 padrão sobrescrito condicionalmente
                 ('resultado="aprovado"; if nota<7: resultado="reprovado"')
                 era marcado como misconception mesmo sendo lido depois --
                 falso positivo grave, corrigido aqui.

            CORREÇÃO (v18): ast.AsyncFor e ast.AsyncWith caíam no ramo
            genérico 'else' (_collect_reads(stmt, ...)), que só registra
            LEITURAS (ctx=Load) -- nunca gerencia 'pending' para as
            atribuições dentro do corpo. Resultado: uma escrita morta
            de verdade dentro de um `async for`/`async with` nunca era
            detectada (a variável nem chegava a entrar em pending), a
            mesma lacuna sistêmica de tratar async como se não existisse
            (já corrigida em A4/C8/D4/B11/G4). Agora ambas reaproveitam
            exatamente a mesma lógica de branch de ast.For/ast.With.
            """
            pending_at_entry = frozenset(pending)

            for stmt in stmts:

                # -- Assign: lê RHS, depois escreve targets --
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

                # -- FunctionDef/AsyncFunctionDef aninhada: não desce, mas
                #    reconhece uso via closure --
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # CORREÇÃO (v12): uma variável do escopo externo lida
                    # dentro de uma função aninhada (closure) é um uso real
                    # -- ex.: 'x = 5; def inner(): print(x); inner()'. A
                    # versão anterior simplesmente ignorava (pass) qualquer
                    # FunctionDef aninhada ao computar leituras, então x
                    # nunca saía de pending e era erroneamente marcado como
                    # "escrita morta / variável nunca usada", mesmo sendo
                    # de fato usada (só que indiretamente, via closure).
                    # Aqui coletamos os nomes lidos (Load) dentro da função
                    # aninhada que NÃO são reatribuídos/parâmetros dela
                    # mesma (ou de funções aninhadas mais profundas) --
                    # esses são variáveis livres que só podem vir do escopo
                    # externo, logo contam como uso real daquele nome.
                    for name in _collect_closure_free_reads(stmt):
                        if name in pending:
                            used.add(name)
                            pending.discard(name)
                        used.add(name)

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

                # -- For/AsyncFor: analisa iter + body + orelse independentes --
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

                # -- With/AsyncWith: analisa context managers + body --
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

                # -- Qualquer outro stmt: apenas registra leituras --
                else:
                    _collect_reads(stmt, used, pending)

            return False

        # ------------------------------------------------------------------
        # Escopo global (top-level)
        # ------------------------------------------------------------------

        # 1. Todas as leituras no arquivo inteiro (incluindo funções)
        #
        # CORREÇÃO (v13): 'x += 1' lê x antes de somar, mas o parser só
        # marca o alvo de AugAssign com ctx=Store, nunca gera um Name com
        # ctx=Load para ele. Sem essa correção, uma variável só usada via
        # AugAssign (ex.: 'total = 0' seguido, em outro lugar do arquivo,
        # só de 'global total; total += n') nunca aparecia em
        # all_file_reads e era erroneamente marcada como nunca lida.
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
        #
        # CORREÇÃO A3 (v13) — BUG GRAVE: 'global'/'nonlocal' eram
        # completamente ignorados. Toda atribuição dentro de uma função
        # era tratada como se fosse sempre uma variável LOCAL, sujeita à
        # regra "precisa ser lida dentro desta mesma função". Isso gerava
        # falso positivo em qualquer função cujo único papel é escrever
        # numa variável de outro escopo (setter/reset/acumulador global):
        #     contador = 0
        #     def resetar():
        #         global contador
        #         contador = 0     # nunca lida DENTRO da função
        #     def mostrar():
        #         print(contador)  # é lida, só que em OUTRA função
        # 'contador = 0' em resetar() entrava em func_pending (nada lê
        # 'contador' no corpo de resetar) e disparava unusedInitVar
        # indevidamente, mesmo a variável sendo genuinamente usada em
        # mostrar(). Agora os nomes declarados via 'global'/'nonlocal' no
        # PRÓPRIO corpo da função (sem descer em funções aninhadas -- cada
        # uma tem sua própria declaração) são pré-marcados como "usados"
        # antes da análise: por definição pertencem a outro escopo, então
        # uma atribuição a eles aqui não é uma "escrita morta local" --
        # quem decide se o valor é ou não usado é o escopo dono da
        # variável (o módulo, ou a função externa em caso de nonlocal).
        def _collect_global_nonlocal_names(funcNode):
            names = set()
            for n in VisitorMC3._iter_own_scope_nodes(funcNode):
                if n is funcNode:
                    continue
                if isinstance(n, (ast.Global, ast.Nonlocal)):
                    names.update(n.names)
            return names

        for node in ast.walk(root):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue

            func_used    = set()
            func_pending = set()

            # Parâmetros já são "conhecidos" — não são escritas pendentes
            for arg in node.args.args:
                func_used.add(arg.arg)

            # Nomes 'global'/'nonlocal' pertencem a outro escopo — não são
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
        """
        A4 — Redefinição de função/variável built-in do Python.

        CORREÇÃO A4 (v14):
            BUG 1 — só reconhecia ast.FunctionDef, nunca
            ast.AsyncFunctionDef. 'async def list(): ...' (e seus
            parâmetros) nunca era verificado, inconsistente com o resto
            do arquivo, onde D4 e G5 já tratam os dois igualmente.

            BUG 2 — só verificava nomes atribuídos via ast.Assign. O
            padrão mais comum de sombrear um builtin em código didático
            costuma ser usar seu nome como variável de iteração de for
            ('for list in itens:'), alvo de 'with ... as'
            ('with open(...) as str:'), nome de exceção capturada
            ('except Exception as dict:'), parâmetro de lambda, ou
            variável de comprehension ('[x for str in itens]') -- nenhum
            desses era verificado, mesmo sendo tão comuns quanto (ou
            mais comuns que) uma atribuição direta. Agora todos são
            tratados como declaração de variável/parâmetro, reaproveitando
            os mesmos conjuntos declaredVariablesAsBuiltIn /
            declaredArgumentsAsBuiltin já expostos pela interface pública.

        CORREÇÃO A4 (v18):
            BUG 3 — ast.For e ast.With eram verificados, mas não suas
            variantes assíncronas ast.AsyncFor/ast.AsyncWith (que não são
            subclasses das síncronas no módulo ast). `async for list in
            gerador():` ou `async with abrir() as str:` sombreando um
            builtin nunca eram detectados -- a mesma lacuna sistêmica já
            corrigida em C8/D4/B11/G4. Agora ambas entram nos mesmos
            ramos que ast.For/ast.With.
        """
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

        for node in ast.walk(root):
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
        """
        A5 — Importação não utilizada. Ignora 'from X import *'.

        CORREÇÃO A5 (v14): used_names coletava QUALQUER ast.Name com
        aquele identificador, sem checar o ctx -- incluindo alvos de
        atribuição (ctx=Store). Isso mascarava o caso de um import
        sombreado/sobrescrito sem nunca ter sido de fato lido:
            import json
            json = 5      # Name(id='json', ctx=Store) -- não é uma
                           # leitura do módulo importado, mas contava
                           # como "uso" e escondia o import morto.
        Agora só ast.Name com ctx=Load conta como uso real.
        """
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
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_names.add(node.id)

        self.unusedImports = list(import_names - used_names)

    # =========================================================================
    # CATEGORIA B
    # =========================================================================

    def checkRepeatedCommandsInIfs(self, root):
        """
        B4 — Comandos repetidos dentro de blocos if/elif/else.

        CORREÇÃO (v17) — falso positivo: um corpo trivial de instrução de
        controle única (pass/return/raise/continue/break) repetido em
        vários ramos de uma mesma cadeia if/elif/else -- ex.:
            if x is None:
                return None
            elif y is None:
                return None
        é um idioma comum e legítimo de guard clause (cada ramo valida
        uma condição independente e reage da mesma forma trivial), não a
        mesma lógica duplicada por engano de copy-paste que esta
        checagem quer capturar. B11 (checkIfsWithSameBody) já exclui
        exatamente esse padrão pela mesma razão; B4 nunca tinha a mesma
        exclusão, então `if a: pass elif b: pass` disparava como falso
        positivo. Agora um ramo com corpo trivial (uma única instrução
        de controle) não entra na comparação de duplicidade.
        """
        def is_trivial_guard(body):
            return (len(body) == 1 and
                    isinstance(body[0], (ast.Return, ast.Raise,
                                          ast.Continue, ast.Break, ast.Pass)))

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
        """
        B6 — Tentativa de usar while como if com condição booleana.

        CORREÇÃO (v10): a versão anterior exigia que o corpo INTEIRO do while
        fosse só break/if-com-break -- se houvesse qualquer outra instrução
        (ex.: um print antes do break), a detecção era cancelada, mesmo que
        o break INCONDICIONAL no final do corpo já garantisse que o loop
        executa no máximo 1 vez (a mesma misconception, só com uma linha a
        mais). Agora a checagem olha só se a ÚLTIMA instrução do corpo é um
        break garantido (direto ou dentro de um if sem alternativa real) --
        o que vier antes não desqualifica mais a detecção.

        CORREÇÃO (v11) — falso positivo do idioma "loop até sentinela":
        a v10 tratava `if cond: break` seguido de `else: pass` (ou sem
        else nenhum) como break "incondicional", só porque o else não
        tinha "trabalho real". Isso está errado: um break dentro de um
        if só acontece quando a condição do if é verdadeira. Um else
        vazio/pass não significa "sempre quebra" -- significa apenas
        "se a condição for falsa, o corpo do if não faz nada especial
        e o while testa de novo normalmente". Isso é exatamente o
        idioma correto e voluntariamente repetitivo de "ler até achar
        um sentinela" (ex.: `while x > 0: valor = obter_proximo(); if
        valor is None: break else: pass`), que pode rodar várias
        iterações antes de quebrar -- não é a mesma coisa que usar
        while no lugar de if.

        Um break dentro de if só é de fato "garantido/incondicional"
        quando TODOS os caminhos possíveis a partir daquele if levam a
        um break -- ou seja, o ramo verdadeiro E o ramo falso (else)
        ambos terminam em break. Se o else estiver ausente ou não
        garantir break, existe um caminho que NÃO quebra o loop, logo
        a saída depende da condição -- não é incondicional.

        CORREÇÃO (v12) — filtro de tipo do `test` deixava passar batido
        o caso mais idiomático da própria misconception: uma variável
        booleana solta (ou sua negação) como condição do while, ex.
        `flag = True; while flag: ...; break` ou `while not flag: ...;
        break`. Antes só (ast.Compare, ast.BoolOp) eram aceitos, então
        ast.Name e ast.UnaryOp(Not) nunca disparavam a checagem. Agora
        um ast.Name solto ou um ast.UnaryOp cujo operador é `not`
        também contam como condição booleana avaliável.
        """
        for node in ast.walk(root):
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
        """
        B8 — If (sozinho ou em cadeia com elif) sem 'else' final.

        CORREÇÃO (v9): antes, só verificava a ausência de else quando já
        existia pelo menos um elif na cadeia (exigia isinstance(node.orelse[0],
        ast.If) antes de entrar no loop). Um 'if' solto, sem elif e sem else,
        nunca era verificado e escapava da detecção mesmo violando o mesmo
        critério (não usar else prejudica legibilidade). Agora todo ast.If,
        com ou sem elif, é verificado quanto à ausência de else final.
        """
        self.nonUtilizationElifElse = False
        for node in ast.walk(root):
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
        """
        B9 — elif retestando condição inversa do if anterior.

        CORREÇÃO B9 (v13): a versão anterior só disparava quando o `if`
        original tinha `test` do tipo ast.Compare puro (uma comparação
        simples, ex.: `x > 5`). Uma condição composta com `and`/`or`
        (ast.BoolOp) nunca entrava na checagem -- o `if` de guarda
        `isinstance(node.test, ast.Compare)` já bloqueava, então
        um caso como:
            if x > 5 and y < 3:
                ...
            elif x <= 5 or y >= 3:   # negação exata via De Morgan
                ...
        passava batido, mesmo sendo a mesma misconception só que
        envolvendo uma expressão composta. Agora, quando o `if` original
        é um ast.BoolOp, tentamos negá-lo estruturalmente aplicando De
        Morgan recursivamente (and<->or, cada operando negado) e
        comparamos essa negação (via ast.dump) com o test do elif.
        Quando a expressão não pode ser negada com segurança (chamada
        de função, comparação encadeada com múltiplos operadores etc.),
        _negate_test retorna None e a checagem simplesmente não dispara
        para aquele ramo -- em vez de arriscar uma negação incorreta.

        O comportamento original (mainTest Compare simples, buscando a
        inversa dentro do elif, mesmo que aninhada em um BoolOp maior
        do elif) é mantido sem alterações.
        """
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

        for node in ast.walk(root):
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
        """
        B10 — elif/else desnecessário após bloco if/elif/else vazio ou com
        apenas pass.

        CORREÇÃO (v10): a versão anterior checava o if vazio com orelse
        depois, e o elif vazio -- mas nunca checava o caso espelhado: um
        'else' final (não elif) vazio ou só com pass, depois de um if com
        conteúdo real. Ex.: 'if erro: processar() else: pass' não era detectado,
        mesmo sendo exatamente a mesma ideia de branch inútil.
        """
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
                if node.orelse:
                    if isinstance(node.orelse[0], ast.If):
                        if is_empty_or_pass_only(node.orelse[0].body):
                            self.unnecessaryElifElse = True
                            return
                    else:
                        # 'else' de verdade (não elif) -- checa se está vazio/pass-only
                        if is_empty_or_pass_only(node.orelse):
                            self.unnecessaryElifElse = True
                            return

    def checkIfsWithSameBody(self, root):
        """
        B11 — Ifs distintos com blocos de código idênticos.

        CORREÇÃO (v10), dois problemas:
        1) Falso positivo: dois ifs de condições completamente diferentes,
           mas com corpo trivial igual por coincidência (ex.: dois guard
           clauses "return None" pra validar variáveis diferentes), eram
           marcados como duplicação -- mas isso é um idioma comum de
           validação independente, não a mesma lógica repetida por engano.
           Agora corpos triviais de uma única instrução de controle
           (return/raise/continue/break/pass) são ignorados na comparação.
        2) Falso negativo: a recursão para dentro de escopos não incluía
           ast.ClassDef, então ifs duplicados dentro de métodos de classe
           nunca eram vistos.

        CORREÇÃO (v17) — falso negativo: a lista de tipos em que a
        recursão desce não incluía ast.AsyncFor nem ast.AsyncWith (só as
        variantes síncronas For/With). Como ast.AsyncFor e ast.AsyncWith
        não são subclasses de ast.For/ast.With no módulo ast, ifs
        duplicados dentro do corpo de um `async for`/`async with` nunca
        eram vistos -- a mesma classe de lacuna de A4/D4/G5/C8 (funções e
        estruturas assíncronas tratadas como se não existissem). Agora
        ambas entram na lista de tipos que a recursão atravessa.
        """
        self.sameBodyIfs = False

        def is_trivial_guard(body):
            return (len(body) == 1 and
                    isinstance(body[0], (ast.Return, ast.Raise,
                                          ast.Continue, ast.Break, ast.Pass)))

        def check_scope(node):
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
        """
        B12 — Ifs consecutivos com a mesma condição mas ações distintas.

        CORREÇÃO (v12): ao comparar um par (firstIf, secondIf) que NÃO
        batia, o código anterior sempre zerava 'conseqIf' incondicional-
        mente -- ou seja, descartava totalmente o 'secondIf' em vez de
        deixá-lo disponível como o próximo 'firstIf' a comparar com o if
        seguinte. Isso quebra cadeias de 3+ ifs consecutivos onde o par
        que bate não é o primeiro: em
            if a: ...
            if b: ...
            if b: ...
        o par (1º,2º) não bate (a != b) e reiniciava a busca a partir do
        3º if sozinho, nunca comparando o 2º com o 3º -- perdendo a
        detecção real do par (2º,3º) que de fato repete a condição 'b'.
        Agora, quando o par não bate, o 'secondIf' (se também não tiver
        orelse) passa a ser o novo 'firstIf' para a próxima comparação,
        em vez de reiniciar o rastreamento do zero.
        """
        def same_test(a, b):
            if isinstance(a, ast.Name) and isinstance(b, ast.Name):
                return a.id == b.id
            if isinstance(a, ast.Compare) and isinstance(b, ast.Compare):
                L = VisitorMC3Helper.compare_ast_nodes(a.left, b.left)
                O = VisitorMC3Helper.compare_ops_equal(a.ops, b.ops)
                R = VisitorMC3Helper.compare_comparators(a.comparators, b.comparators)
                return L and O and R
            return False

        for node in ast.walk(root):
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
        """
        C1 — Condição do while retestada dentro do próprio corpo.

        CORREÇÃO C1 (v9):
            PROBLEMA 1 — só olhava o primeiro nível do corpo (`for item in
            node.body`): um `if` retestando a condição dentro de um `for`,
            `try`, `with` etc. aninhado no corpo do `while` passava
            despercebido. Agora usa _walk_ordered_stmts para descer em
            qualquer bloco composto aninhado.

            PROBLEMA 2 — compare_ast_nodes só reconhecia ast.Name e
            ast.Constant no lado esquerdo da comparação; uma chamada de
            método (ex: contador.valor()) nunca batia, mesmo sendo
            exatamente a mesma expressão nos dois lados. Corrigido em
            compare_ast_nodes com um fallback estrutural genérico.
        """
        for node in ast.walk(root):
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
        """
        C2 — Loop redundante (executa exatamente uma vez).

        CORREÇÃO C2 (v13): a versão anterior só reconhecia `while True:`
        cujo `break` estivesse SOLTO, como statement direto do corpo
        (`for item in node.body: if isinstance(item, ast.Break)`). Um
        break garantido mas aninhado dentro de um `if` -- o caso mais
        comum na prática, ex.:
            while True:
                print("executa uma vez")
                if True:
                    break
        nunca era detectado, mesmo sendo exatamente a mesma misconception
        (loop que sempre quebra na 1ª iteração). Agora reaproveita
        _has_break_no_loop_all (o mesmo helper de B6) para reconhecer
        break garantido em TODO caminho de execução do corpo, incluindo
        dentro de if/else aninhados, sem atravessar loops internos.
        """
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Constant) and node.test.value is True:
                    if VisitorMC3._has_break_no_loop_all(node.body):
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
        """
        C3 — Operações idênticas repetidas dentro do loop.

        CORREÇÃO C3 (v9):
            PROBLEMA 1 — só verificava isinstance(stmt, (ast.Assign, ast.Expr)),
            nunca ast.AugAssign. `soma += i` seguido de `soma += i` (o erro
            de copy-paste mais comum em acumuladores) não era detectado,
            enquanto a forma equivalente `soma = soma + i` era. Corrigido
            incluindo ast.AugAssign na checagem.

            PROBLEMA 2 — só olhava statements diretos de node.body: uma
            duplicação dentro de um `if`/`try`/`with` aninhado no corpo do
            loop não era vista. Corrigido verificando cada lista de
            statements (a do loop e as de cada bloco aninhado) de forma
            recursiva e independente — a checagem continua sendo "duplicata
            dentro do mesmo bloco", sem confundir ramos distintos de um
            if/else (isso é um padrão diferente, não copy-paste).

        CORREÇÃO C3 (v18): o loop externo só verificava ast.For/ast.While
        -- um `async for` nunca era sequer considerado como ponto de
        partida, então duplicação direta no corpo de um `async for`
        (ex.: `soma += item` repetido duas vezes por engano de
        copy-paste) nunca era detectada. Agora ast.AsyncFor também inicia
        a checagem, e o helper _get_child_stmt_lists usado na recursão
        (has_duplicate_in_block) também já reconhece blocos assíncronos
        aninhados.
        """
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

        for node in ast.walk(root):
            if isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
                if has_duplicate_in_block(node.body):
                    self.redundantOpsInLoop = True
                    return

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
        """
        C8 — Variável de iteração do for sobrescrita dentro do loop.

        CORREÇÃO C8 (v9):
            Só verificava statements diretos de node.body: uma sobrescrita
            dentro de um `if`/`try`/`with` aninhado no corpo do `for` não
            era detectada. Corrigido descendo recursivamente em qualquer
            bloco composto aninhado (via _get_child_stmt_lists), mantendo
            o tratamento especial de `for` aninhado (que soma sua própria
            variável de iteração ao escopo antes de checar seu corpo).

        CORREÇÃO C8 (v10): ast.AsyncFor é uma classe separada de
        ast.For no módulo ast (não é subclasse), então `async for i in
        gerador(): i = 99` nunca era visto por esta checagem. Corrigido
        tratando ast.AsyncFor da mesma forma que ast.For em todos os
        pontos: no `for` externo que percorre o módulo, no caso de
        aninhamento recursivo dentro de check_body, e em getVarIter.
        """
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

        for node in ast.walk(root):
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
        """
        Como ast.walk, mas NÃO desce dentro de FunctionDef/AsyncFunctionDef
        aninhadas a partir daqui. Usado para nunca misturar o escopo de uma
        função com o de outra função definida dentro dela (ex: uma
        atribuição feita só dentro de uma função aninhada não pode contar
        como variável local da função externa).
        """
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
        """
        D4 — Função acessando variáveis do escopo externo (global).

        CORREÇÃO D4 (v10):
            BUG 1 — getLocalVars usava ast.walk(funcNode), que desce dentro
            de funções aninhadas definidas no corpo da função analisada.
            Uma atribuição feita só na função interna era incorretamente
            contada como variável local da função externa, escondendo o
            uso real de uma global com o mesmo nome. Corrigido usando
            _iter_own_scope_nodes, que para de descer em FunctionDef/
            AsyncFunctionDef aninhadas. O mesmo helper agora também é
            usado para enumerar os statements a checar (antes usava
            ast.walk(item) por item do corpo, que tinha o mesmo problema).

            BUG 2 — só reconhecia ast.FunctionDef; uma `async def` nunca
            era analisada (nem excluída corretamente do escopo global em
            getGlobalVars). Corrigido tratando FunctionDef e
            AsyncFunctionDef da mesma forma nos dois lugares.

            BUG 3 — em um Assign, só o lado direito (stm.value) era
            verificado; escrever num índice/atributo de uma global
            (`dados[0] = 99`, `obj.attr = 99`) não contava como uso, pois
            o Name-base desses targets nunca era olhado. Corrigido
            verificando os targets também (usando o ctx do Name para
            distinguir a base lida, ctx=Load, do nome realmente atribuído,
            ctx=Store). O mesmo vale agora para o target de AugAssign.

            BUG 4 — ast.Assert e ast.With não eram reconhecidos por
            checkVarUsage; `assert X > 0` e `with open(PATH):` usando uma
            global não eram detectados. Corrigido adicionando os dois
            (e, na mesma linha de raciocínio, ast.Raise e ast.Delete).

        CORREÇÃO D4 (v14) — BUG 5, falso negativo:
            getLocalVars decide o que é "local" varrendo TODA a função de
            uma vez (não é sensível a fluxo/ordem). Uma função que declara
            'global x' e também reatribui x em algum ponto do corpo tinha
            x adicionado a localVars por causa dessa atribuição -- e, como
            a checagem não é sensível a fluxo, isso mascarava QUALQUER
            leitura de x na função inteira, mesmo leituras ANTES da
            reatribuição ou na própria expressão que a calcula:
                total = 0
                def somar(n):
                    global total
                    total = total + n   # lê 'total' (global) e reescreve
            Como 'total' também é alvo de Assign nesta função, entrava em
            localVars e a leitura de 'total' no lado direito nunca era
            reconhecida como acesso a variável externa -- falso negativo
            do padrão mais comum de acumulador global. Corrigido: nomes
            declarados via 'global'/'nonlocal' no próprio corpo da função
            são removidos de localVars ao final, independentemente de
            também aparecerem como alvo de atribuição -- por definição
            pertencem a outro escopo durante toda a execução da função.

        CORREÇÃO D4 (v15) — BUG 6: checkVarUsage só reconhecia
        ast.For; o `.iter` de um `async for` nunca era verificado, então
        uma leitura de global no iterável de um `async for` (ex.
        `async for i in gerador(limite):`, onde `limite` é global) não
        era detectada. Corrigido tratando ast.AsyncFor igual a ast.For.
        """
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
        for node in ast.walk(root):
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
        """
        E1 — Verificação excessiva de combinações.

        CORREÇÃO E1 (v10):
            Antes só cobria o padrão (a) abaixo. O padrão (b) — que é o
            que dá nome à própria misconception — nunca era verificado.

            (a) Uma única condição com muitos termos booleanos encadeados:
                if a and b and c and d and e and f: ...

            (b) Uma cadeia de if/elif enumerando manualmente TODAS as
                2**n combinações de um pequeno conjunto de n variáveis
                booleanas, quando a lógica poderia ser simplificada:
                    if a and b: ...
                    elif a and not b: ...
                    elif not a and b: ...
                    elif not a and not b: ...
                Detecção: para cada cadeia de if/elif, cada ramo é
                decomposto em conjunções (`and`/`not`) de "átomos"
                (comparações, variáveis etc. comparadas estruturalmente
                via ast.dump). Se todos os ramos usam exatamente o mesmo
                conjunto de n>=2 átomos, cada ramo é uma combinação
                distinta de sinais (positivo/negado) desses átomos, e o
                número de ramos é exatamente 2**n, então a cadeia cobre
                exaustivamente todas as combinações -- sinal desse
                misconception. Ramos com `or` são ignorados (a checagem
                é conservadora, focada no padrão de conjunções).
        """
        self.excessiveCombinationChecks = False

        # --- padrão (a): condição única com BoolOp grande ---
        for node in ast.walk(root):
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

        # CORREÇÃO E1 (v16) — BUG: normalize_atom só reconhecia negação
        # explícita via `not`. A forma mais comum, na prática, de escrever
        # esta misconception usa negação por OPERADOR DE COMPARAÇÃO
        # invertido, não `not`:
        #     if idade >= 18 and renda >= 5000: ...
        #     elif idade >= 18 and renda < 5000: ...
        #     elif idade < 18 and renda >= 5000: ...
        #     elif idade < 18 and renda < 5000: ...
        # Aqui `idade < 18` é semanticamente a negação de `idade >= 18`,
        # mas como átomo bruto (ast.dump) são nós Compare diferentes, então
        # nunca eram reconhecidos como "o mesmo átomo, sinal oposto" -- a
        # cadeia inteira era descartada por não ter conjunto de átomos
        # consistente entre os ramos. Agora um Compare de operador único
        # reaproveita VisitorMC3Helper.get_inverse_op (já usado por B12)
        # para normalizar para uma forma canônica (sempre o operador cujo
        # tipo teria menor posição na lista de tipos ordenada) mais uma
        # flag de negação, de modo que operadores opostos no mesmo par
        # left/right colapsem no mesmo átomo.
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

        for node in ast.walk(root):
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
        """
        E2 — Uso excessivo de listas (>= threshold listas declaradas).

        CORREÇÃO E2 (v10): só reconhecia listas literais (`[...]`/list
        comprehension). A criação equivalente via `list()` não era
        contada, mesmo sendo igualmente comum entre alunos.

        CORREÇÃO E2 (v17): só reconhecia ast.Assign. Uma declaração
        anotada com tipo (ex. `numeros: list = []`, comum em cursos que
        já introduzem type hints) é ast.AnnAssign, um nó totalmente
        diferente de ast.Assign -- nunca contava para o total. Agora
        ast.AnnAssign com valor atribuído também é verificado.
        """
        def is_list_creation(value):
            if isinstance(value, (ast.List, ast.ListComp)):
                return True
            if (isinstance(value, ast.Call) and isinstance(value.func, ast.Name)
                    and value.func.id == "list"):
                return True
            return False

        numLists = 0
        for node in ast.walk(root):
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
        """
        G4 — Variáveis/funções com nomes não significativos (muito curtos).
        Correção G4c (v5) mantida: '_' excluído como convenção de descarte.

        CORREÇÃO G4 (v17) — falso negativo: collectFunctionNames e
        collectParamNames só reconheciam ast.FunctionDef. Uma `async def`
        com nomes de função/parâmetro curtos (ex. `async def f(x, y):`)
        nunca era contabilizada -- a mesma lacuna sistêmica de tratar
        funções assíncronas como se não existissem (já corrigida em
        A4/D4/G5/C8/B11). Agora ambas as funções tratam
        ast.AsyncFunctionDef da mesma forma que ast.FunctionDef.
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

        def isDunderMethod(name):
            """
            CORREÇÃO: método mágico do Python (__init__, __str__, __eq__ etc.)
            não é uma escolha de nomenclatura do aluno -- é sintaxe obrigatória
            da linguagem para implementar construtores, representações,
            comparadores, operadores, etc. Contar esses nomes como 'não
            significativos definidos pelo usuário' é incoerente com o próprio
            critério do G4.
            """
            return name.startswith("__") and name.endswith("__") and len(name) > 4

        def collectFunctionNames(root):
            names = []
            for node in ast.walk(root):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if node.name not in names and not isDunderMethod(node.name):
                        names.append(node.name)
            return names

        def collectParamNames(root):
            names = []
            for node in ast.walk(root):
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

        CORREÇÃO G5c (v6): ast.ClassDef era tratado como "código
        executável", disparando falso positivo em qualquer arquivo que
        declarasse uma classe auxiliar antes de uma função -- um padrão
        de organização perfeitamente normal (ex. `class Helper: ...`
        seguido de `def main(): ...`). A misconception que G5 quer
        capturar é código de nível de módulo com efeito real (print,
        loop, atribuição) executando antes das definições de função --
        não outra declaração. Agora ClassDef é tratado como declaração,
        igual a FunctionDef/AsyncFunctionDef.
        """
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
        """
        H1 — Statement sem efeito.

        CORREÇÃO H1 (v10):
            BUG 1 — só reconhecia um literal (número/bool/None) sozinho
            numa linha. O padrão mais comum e mais didático dessa
            misconception -- uma COMPARAÇÃO solta no lugar de uma
            atribuição por engano de digitação (`x == 5` em vez de
            `x = 5`) -- nunca era detectado, assim como um nome solto
            (`x`) ou uma expressão aritmética/booleana solta (`x + 1`,
            `a and b`). Agora um Expr cujo valor seja Compare, Name,
            BinOp ou BoolOp também conta como "sem efeito".

            BUG 2 — Ellipsis (`...`) sozinho era tratado como constante e
            caía na regra, mas é o idioma padrão para stub de função ou
            método abstrato (equivalente a `pass`) -- não é um erro do
            aluno. Agora é explicitamente excluído, assim como strings
            (docstrings/comentários de bloco) já eram.

            BUG 3 (v11) — ast.UnaryOp (ex. `not flag`, `-x` soltos numa
            linha, sem atribuição nem uso) ficava de fora da tupla,
            deixando escapar exatamente o mesmo tipo de erro dos outros
            casos, só que com um operador unário. Nenhuma exclusão
            especial é necessária aqui (diferente de Constant), então
            basta incluir ast.UnaryOp na tupla.
        """
        NO_EFFECT_EXPR_TYPES = (ast.Compare, ast.Name, ast.BinOp, ast.BoolOp, ast.UnaryOp)
        for node in ast.walk(root):
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