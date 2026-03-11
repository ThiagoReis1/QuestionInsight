from numpy import*
from numpy.linalg import*

matriz = array(eval(input("M: ")))
lin = shape(matriz)[0]
col = shape(matriz)[1]
maior = 0
indice = 0
for i in range (lin):
	for j in range (col):
		if matriz[i][j] >maior:
			indice= j
			maior = matriz[i][j]
		else:
			j=j+1
			
print(maior)