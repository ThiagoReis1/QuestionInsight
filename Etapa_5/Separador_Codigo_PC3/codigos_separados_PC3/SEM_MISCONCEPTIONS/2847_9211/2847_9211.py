from numpy import *
vetor = array(eval(input("v:")))
saida = zeros(size(vetor),dtype=int)
for i in range (size(vetor)):
	saida[i] = vetor[i] ** 2
print(saida)