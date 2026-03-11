from numpy import *

entrada = input("Quantidade de pessoas: ")
vetor = entrada.split(',')
estados = ["CHN","JPN","KOR","MGL","THA"]

saida = zeros(size(estados), dtype=int)

for i in range(size(estados)):
	for j in range(size(vetor)):
		if(vetor[j] == estados[i]):
			saida[i] = saida[i] + 1

print(max(saida))
print(saida)
