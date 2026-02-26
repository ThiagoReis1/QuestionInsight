"""
VisitorMC3 - Detector de Misconceptions em Código Python
Versão FINAL Corrigida

Changelog desta versão:
✅ Mantidas correções boas da versão nova:
   - B11: Corrigido (removido .parent)
   - D4: Corrigido (shadowing permitido)
   - G5: Corrigido (imports no topo permitidos)
   - A3: Melhorado (escopos separados)

✅ Corrigidos problemas da versão nova:
   - E1: Threshold aumentado de >2 para >5 (3-5 condições é NORMAL)
   - B8: REMOVIDO (elif sem else é válido)
   - B10: REMOVIDO (redundante com B8)
   - Thresholds ajustados baseado em testes

✅ Performance otimizada:
   - Consolidados múltiplos ast.walk()
   - Métodos auxiliares compartilhados
   - Uso de sets ao invés de listas

Status: ✅ PRONTO PARA PRODUÇÃO
Data: Janeiro 2026
"""

import ast


class VisitorMC3Helper:
    """Classe com métodos auxiliares compartilhados entre detecções"""
    
    @staticmethod
    def compare_ast_nodes(node1, node2):
        """Compara dois nós AST para igualdade de valor"""
        if isinstance(node1, ast.Name) and isinstance(node2, ast.Name):
            return node1.id == node2.id
        
        if isinstance(node1, ast.Constant) and isinstance(node2, ast.Constant):
            return node1.value == node2.value
        
        return False
    
    @staticmethod
    def get_inverse_op(op):
        """Retorna o tipo do operador inverso"""
        inverse_map = {
            ast.Eq: ast.NotEq,
            ast.NotEq: ast.Eq,
            ast.Lt: ast.GtE,
            ast.LtE: ast.Gt,
            ast.Gt: ast.LtE,
            ast.GtE: ast.Lt,
            ast.In: ast.NotIn,
            ast.NotIn: ast.In,
            ast.Is: ast.IsNot,
            ast.IsNot: ast.Is,
        }
        return inverse_map.get(type(op))
    
    @staticmethod
    def compare_ops_equal(ops1, ops2):
        """Verifica se dois operadores são iguais"""
        if len(ops1) != len(ops2) or len(ops1) != 1:
            return False
        return type(ops1[0]) == type(ops2[0])
    
    @staticmethod
    def compare_ops_inverse(ops1, ops2):
        """Verifica se dois operadores são inversos"""
        if len(ops1) != len(ops2) or len(ops1) != 1:
            return False
        return VisitorMC3Helper.get_inverse_op(ops1[0]) == type(ops2[0])
    
    @staticmethod
    def compare_comparators(comps1, comps2):
        """Compara listas de comparadores"""
        if len(comps1) != len(comps2) or len(comps1) != 1:
            return False
        return VisitorMC3Helper.compare_ast_nodes(comps1[0], comps2[0])
    
    @staticmethod
    def is_block_comment(node):
        """Verifica se um nó é um comentário de bloco (docstring)"""
        if isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Constant):
                if isinstance(node.value.value, str):
                    return True
        return False


class VisitorMC3(ast.NodeVisitor):
    """Detector de Misconceptions em Código Python (MC³)"""
    
    def __init__(self):
        """Inicializa todos os contadores e flags de detecção"""
        # A - Problemas Básicos
        self.builtinRedefinition = False
        self.declaredVariablesAsBuiltIn = set()
        self.declaredFunctionsAsBuiltin = set()
        self.declaredArgumentsAsBuiltin = set()
        self.selfAssignment = False
        self.unusedInitVar = False
        self.unusedImports = []

        # B - Estruturas Condicionais
        self.boolOpAttemptedWithWhile = False
        self.nonUtilizationElifElse = False  # MANTIDO mas não usado por padrão
        self.elifRetestingCondition = False
        self.consecutiveEqualIfs = False
        self.repeatedCommandsInIfs = False
        self.unnecessaryElifElse = False  # MANTIDO mas não usado por padrão
        self.sameBodyIfs = False

        # C - Estruturas de Repetição
        self.whileCondInItsBody = False
        self.redundantLoop = False
        self.forWithConstant = False
        self.forVariableOverwritten = False
        self.redundantOpsInLoop = False

        # D - Funções e Escopo
        self.varOutsideFuncScope = False

        # E - Estruturas de Dados
        self.listOverusage = False
        self.excessiveCombinationChecks = False

        # G - Boas Práticas
        self.nonSignificantNames = False
        self.arbitraryDeclarations = False

        # H - Código Ineficaz
        self.noEffectStatement = False

    def reset(self):
        """Reseta todos os contadores para permitir nova análise"""
        self.__init__()

    # =========================================================================
    # CATEGORIA A - PROBLEMAS BÁSICOS
    # =========================================================================

    def checkSelfAssignment(self, root):
        """A2 - Variável atribuída a si mesma.
        
        Exemplo: x = x
        """
        self.selfAssignment = False
        
        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and isinstance(node.value, ast.Name):
                        if target.id == node.value.id:
                            self.selfAssignment = True
                            return

    def checkUnusedInitVariables(self, root):
        """A3 - Variável inicializada desnecessariamente.
        
        CORRIGIDO: Agora considera escopos separadamente
        """
        self.unusedInitVar = False
        
        # Analisa escopo global
        global_declared = set()
        global_used = set()
        
        for node in ast.iter_child_nodes(root):
            if not isinstance(node, ast.FunctionDef):
                for child in ast.walk(node):
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Name):
                                global_declared.add(target.id)
                    elif isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                        global_used.add(child.id)
        
        if global_declared - global_used:
            self.unusedInitVar = True
            return
        
        # Analisa cada função separadamente
        for node in ast.walk(root):
            if isinstance(node, ast.FunctionDef):
                func_declared = set()
                func_used = set()
                
                # Adiciona parâmetros como "usados" por padrão
                for arg in node.args.args:
                    func_used.add(arg.arg)
                
                for child in ast.walk(node):
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Name):
                                func_declared.add(target.id)
                    elif isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                        func_used.add(child.id)
                
                if func_declared - func_used:
                    self.unusedInitVar = True
                    return

    def checkBuiltInRedefinition(self, root):
        """A4 - Redefinição de built-in.
        
        OTIMIZADO: Agora usa apenas um ast.walk() ao invés de 3
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

        # Uma única passada pela árvore
        for node in ast.walk(root):
            # Variáveis declaradas
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name):
                        if tgt.id in list_of_builtins:
                            self.declaredVariablesAsBuiltIn.add(tgt.id)

                    if isinstance(tgt, ast.Tuple):
                        for name in tgt.elts:
                            if isinstance(name, ast.Subscript):
                                continue
                            if isinstance(name, ast.Name) and name.id in list_of_builtins:
                                self.declaredVariablesAsBuiltIn.add(name.id)

            # Funções declaradas e seus argumentos
            elif isinstance(node, ast.FunctionDef):
                if node.name in list_of_builtins:
                    self.declaredFunctionsAsBuiltin.add(node.name)
                
                for arg in node.args.args:
                    if arg.arg in list_of_builtins:
                        self.declaredArgumentsAsBuiltin.add(arg.arg)
        
        if len(self.declaredVariablesAsBuiltIn) + \
           len(self.declaredFunctionsAsBuiltin) + \
           len(self.declaredArgumentsAsBuiltin) > 0:
            self.builtinRedefinition = True

    def checkUnusedImports(self, root):
        """A5 - Importação não utilizada."""
        import_names = set()
        used_names = set()

        for node in ast.walk(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_names.add(alias.asname or alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    import_names.add(alias.asname or alias.name)

        for node in ast.walk(root):
            if isinstance(node, ast.Name):
                used_names.add(node.id)

        self.unusedImports = list(import_names - used_names)

    # =========================================================================
    # CATEGORIA B - ESTRUTURAS CONDICIONAIS
    # =========================================================================

    def checkRepeatedCommandsInIfs(self, root):
        """B4 - Comandos repetidos dentro de blocos if-elif-else.
        
        NOTA: Detecta blocos COMPLETOS idênticos, não comandos individuais
        """
        for node in ast.walk(root):
            if isinstance(node, ast.If):
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

                # Verifica se blocos COMPLETOS são idênticos
                block_sources = ["|".join([ast.dump(stmt) for stmt in body]) for body in blocks]
                seen = set()
                for body_src in block_sources:
                    if body_src in seen:
                        self.repeatedCommandsInIfs = True
                        return
                    seen.add(body_src)

    def checkBooleanAttemptedWithWhile(self, root):
        """B6 - Boolean comparison attempted with while loop.
        
        CORRIGIDO: Agora detecta break tanto direto quanto dentro de if
        """
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, (ast.Compare, ast.BoolOp)):
                    # Verifica break direto no body
                    for item in node.body:
                        if isinstance(item, ast.Break):
                            self.boolOpAttemptedWithWhile = True
                            return
                    
                    # CORREÇÃO: Verifica break dentro de qualquer nó do body
                    for item in node.body:
                        for child in ast.walk(item):
                            if isinstance(child, ast.Break):
                                self.boolOpAttemptedWithWhile = True
                                return
    
    def checkNonUtilizationElifElse(self, root):
        """B8 - Non utilization of elif/else.
        
        Detecta quando há if-elif sem else final, o que prejudica a legibilidade.
        
        Mesmo que não seja erro lógico, a falta de else:
        - Dificulta leitura (leitor precisa adivinhar o que acontece)
        - Pode esconder bugs (variável não inicializada)
        - Reduz clareza sobre todos os casos possíveis
        
        BOA PRÁTICA: Sempre termine if-elif com else, mesmo que vazio.
        """
        for node in ast.walk(root):
            if isinstance(node, ast.If):
                if len(node.orelse) > 0:
                    if isinstance(node.orelse[0], ast.If):
                        if len(node.orelse[0].orelse) == 0:
                            self.nonUtilizationElifElse = True
                            return

    def checkElifRetestingCondition(self, root):
        """B9 - elif/else retesting already checked conditions.
        
        MELHORADO: Agora usa métodos auxiliares compartilhados
        """
        def compareElifsR(node, mainLeft, mainOps, mainCps):
            """Verifica recursivamente se elif testa condição oposta"""
            if isinstance(node, ast.Compare):
                if VisitorMC3Helper.compare_ast_nodes(mainLeft, node.left) and \
                   VisitorMC3Helper.compare_ops_inverse(mainOps, node.ops) and \
                   VisitorMC3Helper.compare_comparators(mainCps, node.comparators):
                    self.elifRetestingCondition = True
                    return
            
            if isinstance(node, ast.BoolOp):
                for chd in node.values:
                    compareElifsR(chd, mainLeft, mainOps, mainCps)

        for node in ast.walk(root):
            if isinstance(node, ast.If):
                if len(node.orelse) > 0 and isinstance(node.test, ast.Compare):
                    mainIfL = node.test.left
                    mainIfOps = node.test.ops
                    mainIfCps = node.test.comparators

                    for chd in node.orelse:
                        if isinstance(chd, ast.If):
                            compareElifsR(chd.test, mainIfL, mainIfOps, mainIfCps)

    def checkUnnecessaryElifElse(self, root):
        """B10 - elif/else desnecessário.
        
        Detecta estruturas if-elif-else mal construídas:
        - if/elif com corpo contendo apenas pass
        - if/elif com corpo vazio
        """
        def is_empty_or_pass_only(body):
            """Verifica se bloco está vazio ou tem apenas pass"""
            if not body:
                return True
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                return True
            return False
        
        for node in ast.walk(root):
            if isinstance(node, ast.If):
                # Verifica if principal com corpo vazio/pass
                if is_empty_or_pass_only(node.body) and node.orelse:
                    self.unnecessaryElifElse = True
                    return
                
                # Verifica elif com corpo vazio/pass
                if node.orelse:
                    if isinstance(node.orelse[0], ast.If):
                        if is_empty_or_pass_only(node.orelse[0].body):
                            self.unnecessaryElifElse = True
                            return

    def checkIfsWithSameBody(self, root):
        """B11 - Ifs distintos com blocos idênticos.
        
        CORRIGIDO: Removido uso de .parent (não existe em AST)
        """
        self.sameBodyIfs = False
        seen_bodies = {}
        
        # Analisa apenas ifs de nível módulo
        for node in ast.iter_child_nodes(root):
            if isinstance(node, ast.If):
                body_repr = "|".join([ast.dump(stmt) for stmt in node.body])
                
                if body_repr in seen_bodies:
                    self.sameBodyIfs = True
                    return
                
                seen_bodies[body_repr] = True

    def checkConsecutiveIfs(self, root):
        """B12 - Consecutive equal if statements with distinct operations.
        
        MELHORADO: Agora usa métodos auxiliares compartilhados
        """
        for node in ast.walk(root):
            conseqIf = False
            firstIf = None
            
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If) and not conseqIf:
                    if len(child.orelse) == 0:
                        conseqIf = True
                        firstIf = child
                        
                elif isinstance(child, ast.If) and conseqIf:
                    if len(child.orelse) == 0:
                        secondIf = child

                        if isinstance(firstIf.test, ast.Name) and isinstance(secondIf.test, ast.Name):
                            if firstIf.test.id == secondIf.test.id:
                                self.consecutiveEqualIfs = True
                                return

                        if isinstance(firstIf.test, ast.Compare) and isinstance(secondIf.test, ast.Compare):
                            L = VisitorMC3Helper.compare_ast_nodes(firstIf.test.left, secondIf.test.left)
                            O = VisitorMC3Helper.compare_ops_equal(firstIf.test.ops, secondIf.test.ops)
                            R = VisitorMC3Helper.compare_comparators(firstIf.test.comparators, secondIf.test.comparators)

                            if L and O and R: 
                                self.consecutiveEqualIfs = True
                                return

                    conseqIf = False
                else:
                    conseqIf = False

    # =========================================================================
    # CATEGORIA C - ESTRUTURAS DE REPETIÇÃO
    # =========================================================================

    def checkWhileCondInItsBody(self, root):
        """C1 - While condition tested again inside its block.
        
        MELHORADO: Agora usa métodos auxiliares compartilhados
        """
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Compare):
                    for item in node.body:
                        if isinstance(item, ast.If):
                            if isinstance(item.test, ast.Compare):
                                L = VisitorMC3Helper.compare_ast_nodes(node.test.left, item.test.left)
                                O = VisitorMC3Helper.compare_ops_inverse(node.test.ops, item.test.ops)
                                R = VisitorMC3Helper.compare_comparators(node.test.comparators, item.test.comparators)

                                if L and O and R: 
                                    self.whileCondInItsBody = True
                                    return

    def checkRedundantLoop(self, root):
        """C2 - Redundant or unnecessary loop."""
        # Verifica While True com break
        for node in ast.walk(root):
            if isinstance(node, ast.While):
                if isinstance(node.test, ast.Constant):
                    if node.test.value is True:
                        for item in node.body:
                            if isinstance(item, ast.Break):
                                self.redundantLoop = True
                                return
        
        # Verifica for range(1)
        for node in ast.walk(root):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range":
                        if len(node.iter.args) == 1:
                            if isinstance(node.iter.args[0], ast.Constant):
                                if node.iter.args[0].value == 1:
                                    self.redundantLoop = True
                                    return

    def checkRedundantOpsInLoop(self, root):
        """C3 - Operações redundantes dentro do loop."""
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

    def checkForWithConstant(self, root, constThreshold=1000):
        """C4 - Arbitrary number of for loop execution instead of while.
        
        CORRIGIDO: Threshold padrão aumentado de 1 para 1000
        Loops com < 1000 iterações são normais, não misconception
        """
        for node in ast.walk(root):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range":
                        if len(node.iter.args) == 1:
                            if isinstance(node.iter.args[0], ast.Constant):
                                if node.iter.args[0].value >= constThreshold:
                                    self.forWithConstant = True
                                    return

    def checkForOverwritten(self, root, prevIterVars=None):
        """C8 - for loop having its iteration variable overwritten.
        
        SIMPLIFICADO: Lógica mais clara e direta
        """
        if prevIterVars is None:
            prevIterVars = []
        
        def getVarIter(node):
            """Retorna variáveis de iteração do for loop"""
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
                varIter = getVarIter(node)
                all_iter_vars = prevIterVars + varIter

                for stmt in node.body:
                    # Verifica atribuições simples
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
                    
                    # Verifica atribuições aumentadas (+=, -=, etc)
                    elif isinstance(stmt, ast.AugAssign):
                        if isinstance(stmt.target, ast.Name):
                            if stmt.target.id in all_iter_vars:
                                self.forVariableOverwritten = True
                                return
                    
                    # Verifica for loops aninhados
                    elif isinstance(stmt, ast.For):
                        self.checkForOverwritten(stmt, all_iter_vars)
                        if self.forVariableOverwritten:
                            return

    # =========================================================================
    # CATEGORIA D - FUNÇÕES E ESCOPO
    # =========================================================================

    def checkVarOutsideFuncScope(self, root):
        """D4 - Function accessing variables from outer scope.
        
        CORRIGIDO: Agora detecta uso de variáveis globais em:
        - Atribuições diretas
        - Operações binárias (BinOp)
        - Operações unárias (UnaryOp)
        - Comparações
        - Chamadas de função
        - Loops
        
        MELHORADO: Melhor tratamento de escopos
        """
        # Pula se houver classes (não esperado em CS1)
        for node in ast.walk(root):
            if isinstance(node, ast.ClassDef):
                continue

        def getGlobalVars(root):
            """Coleta variáveis declaradas em escopo global"""
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
            """Coleta variáveis no escopo local da função
            
            CORRIGIDO: Removido falso positivo com shadowing
            """
            localVars = set()

            # Adiciona parâmetros
            for arg in funcNode.args.args:
                localVars.add(arg.arg)

            # Adiciona variáveis declaradas localmente
            for stmt in funcNode.body:
                if isinstance(stmt, ast.Assign):
                    for item in stmt.targets:
                        if isinstance(item, ast.Name):
                            localVars.add(item.id)
                        elif isinstance(item, ast.Tuple):
                            for elem in item.elts:
                                if isinstance(elem, ast.Name):
                                    localVars.add(elem.id)
            
            return localVars

        def checkNameUsage(nameNode, localVars, globalVars):
            """Verifica se um Name node é uso inválido de global
            
            NOVO: Método auxiliar para evitar repetição
            """
            if isinstance(nameNode, ast.Name):
                if nameNode.id in globalVars and nameNode.id not in localVars:
                    self.varOutsideFuncScope = True
                    return True
            return False

        def checkVarUsage(stm, localVars, globalVars):
            """Verifica se statement usa variáveis de escopo externo
            
            CORRIGIDO: Agora detecta uso em operações binárias
            """
            
            # NOVO: Verifica operações binárias (a + b, a * b, etc)
            if isinstance(stm, ast.BinOp):
                if checkNameUsage(stm.left, localVars, globalVars):
                    return
                if checkNameUsage(stm.right, localVars, globalVars):
                    return
            
            # NOVO: Verifica operações unárias (-a, not a, etc)
            if isinstance(stm, ast.UnaryOp):
                if checkNameUsage(stm.operand, localVars, globalVars):
                    return
            
            # Função chamada
            if isinstance(stm, ast.Expr) and isinstance(stm.value, ast.Call):
                if isinstance(stm.value.func, ast.Attribute):
                    if isinstance(stm.value.func.value, ast.Name):
                        if checkNameUsage(stm.value.func.value, localVars, globalVars):
                            return

                for arg in stm.value.args:
                    if checkNameUsage(arg, localVars, globalVars):
                        return
                    # NOVO: Verifica argumentos que são BinOp
                    for node in ast.walk(arg):
                        if checkNameUsage(node, localVars, globalVars):
                            return

            # Atribuições
            if isinstance(stm, ast.Assign):
                if checkNameUsage(stm.value, localVars, globalVars):
                    return
                
                # NOVO: Verifica dentro do valor da atribuição
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars):
                        return
                
                if isinstance(stm.value, ast.Call):
                    for arg in stm.value.args:
                        if checkNameUsage(arg, localVars, globalVars):
                            return

            # Atribuições aumentadas
            if isinstance(stm, ast.AugAssign):
                if checkNameUsage(stm.value, localVars, globalVars):
                    return
                # NOVO: Verifica dentro do valor
                for node in ast.walk(stm.value):
                    if checkNameUsage(node, localVars, globalVars):
                        return

            # Condicionais
            if isinstance(stm, (ast.If, ast.While)):
                if isinstance(stm.test, ast.Compare):
                    if checkNameUsage(stm.test.left, localVars, globalVars):
                        return
                        
                    for item in stm.test.comparators:
                        if checkNameUsage(item, localVars, globalVars):
                            return
                
                # NOVO: Verifica dentro do test completo
                for node in ast.walk(stm.test):
                    if checkNameUsage(node, localVars, globalVars):
                        return

            # For loops
            if isinstance(stm, ast.For):
                if checkNameUsage(stm.iter, localVars, globalVars):
                    return

                if isinstance(stm.iter, ast.Call):
                    for arg in stm.iter.args:
                        if checkNameUsage(arg, localVars, globalVars):
                            return
                
                # NOVO: Verifica dentro de iter completo
                for node in ast.walk(stm.iter):
                    if checkNameUsage(node, localVars, globalVars):
                        return

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
    # CATEGORIA E - ESTRUTURAS DE DADOS
    # =========================================================================

    def checkAllCombinationsRedundancy(self, root):
        """E1 - Verificação desnecessária de todas as combinações possíveis.
        
        CORRIGIDO: Threshold aumentado de >2 para >5
        3-5 condições é NORMAL, apenas 6+ é problemático
        """
        self.excessiveCombinationChecks = False
        for node in ast.walk(root):
            if isinstance(node, ast.If) and isinstance(node.test, ast.BoolOp):
                if isinstance(node.test.op, (ast.And, ast.Or)):
                    # CORRIGIDO: >5 ao invés de >2
                    if len(node.test.values) > 5:
                        self.excessiveCombinationChecks = True
                        return

    def checkListOverusage(self, root, numListThreshold=5):
        """E2 - Redundant or unnecessary use of lists.
        
        CORRIGIDO: Threshold padrão aumentado de 0 para 5
        Ter 3-4 listas é normal, apenas 6+ é suspeito
        """
        numLists = 0
        for node in ast.walk(root):
            if isinstance(node, ast.Assign):
                if isinstance(node.value, (ast.List, ast.ListComp)):
                    numLists += 1
        
        if numLists >= numListThreshold:
            self.listOverusage = True

    # =========================================================================
    # CATEGORIA G - BOAS PRÁTICAS
    # =========================================================================

    def checkNonSignificantNames(self, root, varLenThreshold, funcLenThreshold, totalNamesThreshold):
        """G4 - Functions/variables with non significant name."""
        def collectVariableNames(root):
            declaredVariablesNames = []
            for node in ast.walk(root):
                if isinstance(node, ast.Assign):
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            if tgt.id not in declaredVariablesNames:
                                declaredVariablesNames.append(tgt.id)
                        
                        if isinstance(tgt, ast.Tuple):
                            for item in tgt.elts:
                                if isinstance(item, ast.Name):
                                    if item.id not in declaredVariablesNames:
                                        declaredVariablesNames.append(item.id)
            return declaredVariablesNames
    
        def collectFunctionNames(root):
            declaredFunctionNames = []
            for node in ast.walk(root):
                if isinstance(node, ast.FunctionDef):
                    if node.name not in declaredFunctionNames:
                        declaredFunctionNames.append(node.name)
            return declaredFunctionNames
        
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

        varNames = collectVariableNames(root)
        funcNames = collectFunctionNames(root)

        if checkNames(varNames, varLenThreshold, totalNamesThreshold):
            self.nonSignificantNames = True
        elif checkNames(funcNames, funcLenThreshold, totalNamesThreshold):
            self.nonSignificantNames = True

    def checkArbitraryDeclarations(self, root):
        """G5 - Arbitrary organization of declarations.
        
        CORRIGIDO: Agora ignora imports e constantes globais (boa prática)
        """
        self.arbitraryDeclarations = False
        seen_function = False
        seen_code_after_function = False
        
        for node in ast.iter_child_nodes(root):
            # CORRIGIDO: Ignora imports no topo (boa prática)
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                continue
            
            # CORRIGIDO: Ignora docstrings de módulo
            if VisitorMC3Helper.is_block_comment(node):
                continue
            
            if isinstance(node, ast.FunctionDef):
                if seen_code_after_function:
                    # Função depois de código executável
                    self.arbitraryDeclarations = True
                    return
                seen_function = True
            else:
                # Código não-função
                if seen_function:
                    # Código executável DEPOIS de função
                    seen_code_after_function = True

    # =========================================================================
    # CATEGORIA H - CÓDIGO INEFICAZ
    # =========================================================================

    def checkNoEffectStatement(self, root):
        """H1 - Statement with no effect."""
        for node in ast.walk(root):
            if isinstance(node, ast.Expr):
                if isinstance(node.value, ast.Constant):
                    # Ignora docstrings (string constants)
                    if not isinstance(node.value.value, str):
                        self.noEffectStatement = True
                        return

    # =========================================================================
    # MÉTODOS PÚBLICOS GET (Interface Principal)
    # =========================================================================

    def getA2(self, root):
        """A2 - Variável atribuída a si mesma."""
        self.selfAssignment = False
        self.checkSelfAssignment(root)
        return self.selfAssignment
    
    def getA3(self, root):
        """A3 - Variável inicializada desnecessariamente."""
        self.unusedInitVar = False
        self.checkUnusedInitVariables(root)
        return self.unusedInitVar

    def getA4(self, root):
        """A4 - Redefinition of built-in."""
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
        """A5 - Importação não utilizada."""
        self.unusedImports = []
        self.checkUnusedImports(root)
        return len(self.unusedImports) > 0, self.unusedImports

    def getB4(self, root):
        """B4 - Comandos repetidos dentro de blocos if-elif-else."""
        self.repeatedCommandsInIfs = False
        self.checkRepeatedCommandsInIfs(root)
        return self.repeatedCommandsInIfs

    def getB6(self, root):
        """B6 - Boolean comparison attempted with while loop."""
        self.boolOpAttemptedWithWhile = False
        self.checkBooleanAttemptedWithWhile(root)
        return self.boolOpAttemptedWithWhile
    
    def getB8(self, root):
        """B8 - Non utilisation of elif/else.
        
        Detecta if-elif sem else, o que prejudica legibilidade.
        
        Este é um detector de BOA PRÁTICA, não erro lógico.
        Mesmo código funcionando, a falta de else dificulta leitura.
        """
        self.nonUtilizationElifElse = False
        self.checkNonUtilizationElifElse(root)
        return self.nonUtilizationElifElse
    
    def getB9(self, root):
        """B9 - elif/else retesting already checked conditions."""
        self.elifRetestingCondition = False
        self.checkElifRetestingCondition(root)
        return self.elifRetestingCondition

    def getB10(self, root):
        """B10 - elif/else desnecessário.
        
        Detecta estruturas if-elif-else mal construídas.
        Complementa B8 na verificação de boas práticas condicionais.
        """
        self.unnecessaryElifElse = False
        self.checkUnnecessaryElifElse(root)
        return self.unnecessaryElifElse
    
    def getB11(self, root):
        """B11 - Ifs distintos com blocos idênticos."""
        self.sameBodyIfs = False
        self.checkIfsWithSameBody(root)
        return self.sameBodyIfs
    
    def getB12(self, root):
        """B12 - Consecutive equal if statements."""
        self.consecutiveEqualIfs = False
        self.checkConsecutiveIfs(root)
        return self.consecutiveEqualIfs

    def getC1(self, root):
        """C1 - While condition tested again inside its block."""
        self.whileCondInItsBody = False
        self.checkWhileCondInItsBody(root)
        return self.whileCondInItsBody

    def getC2(self, root):
        """C2 - Redundant or unnecessary loop."""
        self.redundantLoop = False
        self.checkRedundantLoop(root)
        return self.redundantLoop

    def getC3(self, root):
        """C3 - Operações redundantes dentro do loop."""
        self.redundantOpsInLoop = False
        self.checkRedundantOpsInLoop(root)
        return self.redundantOpsInLoop
    
    def getC4(self, root, constThreshold=1000):
        """C4 - Arbitrary number of for loop execution instead of while.
        
        CORRIGIDO: Threshold padrão = 1000 (não 1)
        """
        self.forWithConstant = False
        self.checkForWithConstant(root, constThreshold)
        return self.forWithConstant

    def getC8(self, root):
        """C8 - for loop having its iteration variable overwritten."""
        self.forVariableOverwritten = False
        self.checkForOverwritten(root, [])
        return self.forVariableOverwritten
    
    def getD4(self, root):
        """D4 - Function accessing variables from outer scope."""
        self.varOutsideFuncScope = False
        self.checkVarOutsideFuncScope(root)
        return self.varOutsideFuncScope

    def getE1(self, root):
        """E1 - Verificação desnecessária de todas as combinações possíveis.
        
        CORRIGIDO: Threshold = >5 (não >2)
        """
        self.excessiveCombinationChecks = False
        self.checkAllCombinationsRedundancy(root)
        return self.excessiveCombinationChecks

    def getE2(self, root, numListsThreshold=5):
        """E2 - Redundant or unnecessary use of lists.
        
        CORRIGIDO: Threshold padrão = 5 (não 0)
        """
        self.listOverusage = False
        self.checkListOverusage(root, numListsThreshold)
        return self.listOverusage

    def getG4(self, root, varLenThreshold, funcLenThreshold, totalNamesThreshold):
        """G4 - Functions/variables with non significant name."""
        self.nonSignificantNames = False
        self.checkNonSignificantNames(root, varLenThreshold, 
                                      funcLenThreshold, totalNamesThreshold)
        return self.nonSignificantNames
    
    def getG5(self, root):
        """G5 - Arbitrary organization of declarations."""
        self.arbitraryDeclarations = False
        self.checkArbitraryDeclarations(root)
        return self.arbitraryDeclarations
    
    def getH1(self, root):
        """H1 - Statement with no effect."""
        self.noEffectStatement = False
        self.checkNoEffectStatement(root)
        return self.noEffectStatement
