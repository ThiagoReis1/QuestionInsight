from numpy import*

vet = array(eval(input("numeros: ")))
cont = 0

for i in range (size(vet)):
	if vet[i] == 9:
		vet[i] = 0
	else:
		vet[i] = vet[i] + 1
print(vet)		