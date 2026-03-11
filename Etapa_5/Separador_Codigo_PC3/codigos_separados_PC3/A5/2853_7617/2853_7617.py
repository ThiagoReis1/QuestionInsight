# Nelson Geraldo A. de Carvalho

import numpy as np

# Inputs
vetor = eval(input('Digite um vetor: '))

# Variaveis Acumuladoras
soma = 0

# Operacao
for i in range(len(vetor)):
	if vetor[i] == 10:
		soma = (soma) * 10
	else:
		soma = soma + (vetor[i])
	
# Outputs
print(soma)