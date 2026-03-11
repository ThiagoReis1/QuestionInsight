from numpy import*

vet = array(eval(input("digite o vetor: ")))
cont = 0

for i in range(size(vet)):
	vet[i] = vet[i] * vet[i]
	cont = cont + 1
print(vet)