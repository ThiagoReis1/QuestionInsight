import numpy as np

arrQtdAlunos = np.array(eval(input()))
qtdTrios = 0

for i in range(0, arrQtdAlunos.size):	
	if(arrQtdAlunos[i] % 3 == 0):
		qtdTrios += 1
		
arrIndexTrios = np.zeros(qtdTrios, dtype=int)
		
j = 0
for i in range(0, arrQtdAlunos.size):
	if(arrQtdAlunos[i] % 3 == 0):
		arrIndexTrios[j] = i
		j += 1
		
print(qtdTrios)
print(arrIndexTrios)