from numpy import *
cpf = int(input("cpf:"))
vet = len(cpf)
x = 0

if (len(cpf) == 11):
	for i in range(size(vet)):
		if(vet[i] % 2 != 0):
			x = x + 1
	vet2 = zeros(x, dtype = int)

	y = 0

	for j in range(size(vet2)):
		if(vet[j] % 2!= 0):
			vet2[y] = vet[j]
			y = y + 1
	print(vet2)
else:
	print("INVALIDO")