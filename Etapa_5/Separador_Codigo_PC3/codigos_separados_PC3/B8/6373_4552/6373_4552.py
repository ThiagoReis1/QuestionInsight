from numpy import *

entrada = input()

vet = zeros(4, dtype=int)

for letra in entrada.split(","):
	if(letra.upper() == 'A'):
		vet[0] += 1
	elif(letra.upper() == 'P'):
		vet[1] += 1
	elif(letra.upper() == 'D'):
		vet[2] += 1
	elif(letra.upper() == 'M'):
		vet[3] += 1
		
print(vet)
