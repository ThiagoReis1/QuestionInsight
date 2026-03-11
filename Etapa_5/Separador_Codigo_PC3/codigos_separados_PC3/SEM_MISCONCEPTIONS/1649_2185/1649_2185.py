from numpy import * 
entrada  = input("pessoas: ")
vetor = entrada.split(',')
estados = ["P","C","M","V","A"]

saida = zeros(size(estados),dtype = int)

for i in range(size(estados)):
	for j in range(size(vetor)):
		if(vetor[j] == estados[i]):
			saida[i] = saida[i] + 1
print(max(saida))
print(saida)

	
