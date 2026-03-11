from numpy import *
vet1 = input("Digite a cor: ")
vet2 = vet1.split(',')
cores = ["P", "C", "M", "V", "A"]
saida = zeros(size(cores), dtype=int)
for i in range (size(cores)):
	for j in range (size(vet2)):
		if(vet2[j] == cores[i]):
			saida[i] = saida[i] + 1
		
print(max(saida))
print(saida)
