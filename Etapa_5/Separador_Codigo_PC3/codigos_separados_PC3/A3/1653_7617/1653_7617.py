# Nelson Geraldo A. de Carvalho

import numpy as np

nacionalidades = input('Digite uma string contendo as nacionalidades: ').upper()
vet_nacion = nacionalidades.split(',')

contagem = np.zeros(5, dtype=int)

for i in vet_nacion:
	if i == 'AR':
		contagem[0] += 1
	elif i == 'BR':
		contagem[1] += 1
	elif i == 'CL':
		contagem[2] += 1
	elif i == 'CO':
		contagem[3] += 1
	else:
		contagem[4] += 1
		
indice = 0
# a = max(contagem)

for i in range(np.size(contagem)-1):
	if contagem[i] > contagem[i + 1]:
		indice = contagem[i]
		
# Outputs
print(max(contagem))
print(contagem)