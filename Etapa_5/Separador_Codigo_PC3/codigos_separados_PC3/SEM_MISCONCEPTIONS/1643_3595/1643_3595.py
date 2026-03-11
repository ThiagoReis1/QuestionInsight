from numpy import *

vetor = eval(input())
contAprov = 0

for indice in range(len(vetor)):
	if vetor[indice] >= 5:
		contAprov+=1

saida = []*contAprov

for indice in range(len(vetor)):
	if vetor[indice] >= 5:
		saida.append(indice)

print(contAprov)
print(array(saida))