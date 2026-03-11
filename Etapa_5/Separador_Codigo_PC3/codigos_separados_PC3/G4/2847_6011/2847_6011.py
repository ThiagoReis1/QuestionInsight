from numpy import*
vet = array(eval(input("digite o vetor: ")))

for i in range(size(vet)):
	if(vet[i]>=1):
		vet[i] = vet[i] * vet[i]
		i = i +1 
	print(vet)

