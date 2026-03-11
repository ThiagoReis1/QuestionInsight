from numpy import *

vet = array(eval(input("vetor de numeros: ")))

for i in range(size(vet)):
	vet[i] *= 2
	
print(vet)