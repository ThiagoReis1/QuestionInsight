from numpy import *

cabelo = input("cor do cabelo: ").split(' , ')

vet = zeros(5, dtype = int)

for x in cabelo:
	if (x == "P"):
		vet[0] = vet[0] + 1
	elif (x== "C"):
		vet[1] = vet[1] + 1
	elif (x== "R"):
		vet[2] = vet[2] + 1
	elif (x== "L"):
		vet[3] = vet[3] + 1
	elif (x== "B"):
		vet[4] = vet[4] + 1
	
print()
