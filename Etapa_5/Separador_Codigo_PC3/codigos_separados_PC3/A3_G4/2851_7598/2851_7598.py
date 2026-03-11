from numpy import*

vet = array(eval(input("vetor de numeros")))
cont = 0
SOMA = 0

for i in range(size(vet)):
	if(vet[i] == 99):
		SOMA = SOMA *2

	else:
		SOMA = SOMA + vet[i]
		
print(SOMA)