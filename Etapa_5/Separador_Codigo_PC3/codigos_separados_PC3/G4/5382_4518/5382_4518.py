from numpy import *

palavra = input().upper()
vet = list(palavra)

soma = 0.0
cont = 0

while cont < size(vet):
	if vet[cont] == "A" or vet[cont] == "E" or vet[cont] == "I" or vet[cont] == "O" or vet[cont] == "U":
		soma += 0.25
		cont += 1
		
	else:
		soma += 0.27
		cont += 1
		
print(soma)