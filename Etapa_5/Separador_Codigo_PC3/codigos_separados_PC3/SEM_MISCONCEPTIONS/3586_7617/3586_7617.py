# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

# Imports
import numpy as np

# Inputs
acertos = eval(input('Digite um vetor indicando os aneis acertados: '))

# Variaveis Acumuladoras
pontos = 0
i = 0

# Operacao
while i < np.size(acertos):
	if acertos[i] == 1:
		pontos += 100
	elif acertos[i] == 2:
		pontos += 60
	elif acertos[i] == 3:
		pontos += 20
	else:
		pontos += 0
	i += 1

# Output
print(int(pontos))