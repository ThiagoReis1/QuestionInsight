from numpy import*

vet = array(eval(input("digite o vetor: ")))

for i in range(size(vet)):
	vet[i] = vet[i]-1
	if vet[i]<0:
		vet[i] = 9
print(vet)