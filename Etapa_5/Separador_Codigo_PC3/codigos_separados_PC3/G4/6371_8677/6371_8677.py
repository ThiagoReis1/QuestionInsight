from numpy import *

vet = array(eval(input("insira o vetor: ")))

vet1 = zeros(vet, dtype=int)

for i in range(size(vet)):
	if i == vet[0]:
		vet[0] = vet[0] - 1
		vet[0] = vet1[0]
print(vet1)
