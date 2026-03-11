from numpy import *

vet = array(eval(input('Valores: ')))

for i in range(0, size(vet)):
	vet[i] = vet[i] * 2

print(vet)