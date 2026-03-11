from numpy import *

vet = input("Digite o vetor: ").split(',')

vet2 = zeros(5, dtype=int)



for i in range(len(vet)):
	if(vet[i].upper() == "P"):
		vet2[0] = vet2[0] + 1
	elif(vet[i].upper() == "C"):
		vet2[1] = vet2[1] + 1
	elif(vet[i].upper() == "R"):
		vet2[2] = vet2[2] + 1
	elif(vet[i].upper() == "L"):
		vet2[3] = vet2[3] + 1
	elif(vet[i].upper() == "B"):
		vet2[4] = vet2[4] + 1

print(max(vet2))
print(vet2)