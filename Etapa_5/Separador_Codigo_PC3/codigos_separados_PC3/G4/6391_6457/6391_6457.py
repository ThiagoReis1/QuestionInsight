from numpy import *

vet = array(eval(input("Digite o vetor: ")))


for i in range(size(vet)):
	if vet[i] == 0:
		vet[i] = 9 ** 3
	else:
		pred = vet[i] - 1
		vet[i] = pred ** 3	
print(vet) 
		