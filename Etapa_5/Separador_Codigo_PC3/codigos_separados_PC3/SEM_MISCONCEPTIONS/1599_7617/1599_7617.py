# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

# Imports
import numpy as np

# Inputs
custos = eval(input('Digite um vetor com os custos da compra: '))

# custos[i] > 80 = Desconto de 15%
total = 0
i = 0

# Operacao
while i < np.size(custos):
	if custos[i] > 80.0:
		total += custos[i] - (custos[i] * 0.15)
	else:
		total += custos[i]
	i += 1

# Outputs
print(round(total, 2))