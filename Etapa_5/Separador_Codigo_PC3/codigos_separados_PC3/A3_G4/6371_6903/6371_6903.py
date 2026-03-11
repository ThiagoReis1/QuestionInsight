from numpy import *

vet = array(eval(input("insira a senha: ")))
a = 0
for i in range(0,size(vet),1):
	if vet[i] == 0:
		vet[i] = 81
	else:
		vet[i] = vet[i] - 1
		vet[i] = (vet[i])**2

	a = 1
	
print(vet)