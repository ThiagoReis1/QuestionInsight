from numpy import *

vet = array(eval(input("Digite um vetor: ")))

#vet2 = zeros(size(vet), dtype = int)
for i in range(size(vet)):
	if(vet[i] == 0):
		vet[i] = 9
	else:
		vet[i] = vet[i] - 1

print(vet)