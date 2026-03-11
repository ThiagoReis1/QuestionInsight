from numpy import *

vet = array(eval(input("Numeros: ")))

vet_zeros = zeros(size(vet),dtype=int)

for i in range(size(vet)):
	vet_zeros[i] = vet[i] - 1
	if(vet[i] == 0):
		vet_zeros[i] = 9
print(vet_zeros)
	