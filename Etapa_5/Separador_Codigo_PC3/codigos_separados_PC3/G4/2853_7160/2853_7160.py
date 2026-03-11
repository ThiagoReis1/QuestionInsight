from numpy import*

vet = array(eval(input()))

SOMA = 0
x = 0

for i in vet:
	if (vet[x] != 10):
		SOMA = SOMA + vet[x]
	if (vet[x] == 10):
		SOMA = SOMA*10
	x = x + 1
	
print(SOMA)