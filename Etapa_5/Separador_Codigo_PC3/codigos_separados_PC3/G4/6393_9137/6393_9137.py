from numpy import *

vet = array(eval(input()))
nova = zeros(size(vet), dtype=int)

for i in range(size(vet)): #range(vet, 10, -1)
	if vet[i] != 9:
		nova[i] = (vet[i] + 1) ** 3
	else:
		nova[i] = 0
print(nova)