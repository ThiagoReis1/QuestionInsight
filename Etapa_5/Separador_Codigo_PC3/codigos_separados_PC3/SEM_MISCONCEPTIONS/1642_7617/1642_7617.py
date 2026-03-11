# Nelson Geraldo A. de Carvalho

import numpy as np

qtd = eval(input('Digite um vetor contendo a quantidade de alunos matriculados: '))

count_cinco = 0

qtd_zeros = 0
for i in qtd:
	if i % 5 == 0:
		count_cinco += 1
		qtd_zeros += 1	
	
indices = np.zeros(qtd_zeros, dtype=int)

count = 0
for i in range(np.size(qtd)):
	#if qtd[i] % 5 == 0:
		#print(i, qtd[i])
	if qtd[i] % 5 == 0:
		indices[count] = i
		count += 1

# Outputs
print(count_cinco)
print(indices)