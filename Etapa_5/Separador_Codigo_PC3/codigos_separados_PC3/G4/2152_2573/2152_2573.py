from numpy import *

vet = array(eval(input("Entre com o vetor: ")))


cont = zeros(2, dtype=int)

for i in range(size(vet)):
	if (vet[i] % 2 == 0):
		cont[0] = cont[0] + 1
	else:
		cont[1] = cont[1] + 1
print(cont)