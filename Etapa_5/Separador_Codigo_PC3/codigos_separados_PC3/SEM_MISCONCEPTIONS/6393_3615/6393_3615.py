from numpy import *

entrada = array(eval(input()))
vet = zeros(size(entrada), dtype=int)

for i in range(size(entrada)):
	vet[i] = entrada[i]+1
	if vet[i] > 9:
		vet[i] = 0
	else:
		vet[i] = vet[i]**3
print(vet)