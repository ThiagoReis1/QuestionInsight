from numpy import *
entrada = input("Digite um vetor: ")
v = entrada.split(',')
estados = ["AZ","CA","FL","PA","WI"]

saida = zeros(size(estados), dtype = int)

for i in range(size(estados)):
	for j in range(size(v)):
		if(v[j] == estados[i]):
			saida[i] = saida[i] + 1
print(max(saida))
print(saida)