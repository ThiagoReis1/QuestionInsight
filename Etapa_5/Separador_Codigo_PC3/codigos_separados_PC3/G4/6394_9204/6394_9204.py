from numpy import*
vet = array(eval(input("digite o codigo:")))

for i in range(size(vet)):
	if vet[i] == 9:
		vet[i] = 0
	else:
		vet[i] = vet[i] + 1
print(vet)