from numpy import*
from numpy.linalg import*

matriz = array(eval(input("digite: ")))
lin = shape(matriz)[0]
vetor = zeros(lin)

for i in range(lin):
	vetor[i] = min(matriz[i,:])

for i in range(size(vetor)):
	if vetor[i] == min(vetor):
		print(i)