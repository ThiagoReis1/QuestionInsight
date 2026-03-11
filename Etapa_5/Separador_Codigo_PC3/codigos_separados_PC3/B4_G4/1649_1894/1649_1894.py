from numpy import *

vet = input("valor do vetor: ").split(',')

vc = ('P','C','M','V','A')
j = 0

for i in range(size(vet)):
	if(vet[i] == "P"):
		vc[j] = vc[j] + 1
	elif(vet[i] == "C"):
		vc[j] = vc[j] + 1
	elif(vet[i] == "M"):
		vc[j] = vc[j] + 1
	elif(vet[i] == "V"):
		vc[j] = vc[j] + 1
	else:
		vc[j] = vc[j] + 1
print(vc)