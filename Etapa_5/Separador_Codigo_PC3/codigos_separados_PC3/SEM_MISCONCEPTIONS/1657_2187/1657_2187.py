from numpy import *

entrada = input("Entrada: ")

vetor = entrada.split(",")
ESTADOS = ["AZ","CA","FL","PA","WI"]

saida = zeros(size(ESTADOS), dtype = int)


for i in range(size(ESTADOS)):
	for j in range(size(vetor)):
		if(vetor[j] == ESTADOS[i]):
			saida[i] = saida[i] + 1
	
print(max(saida))
print(saida)