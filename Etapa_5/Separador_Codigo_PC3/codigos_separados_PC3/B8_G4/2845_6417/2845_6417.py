from numpy import *

vet = array(eval(input("Entrada: ")))
n = size(vet)

for i in range(0,n):
	if vet[i] == 9:
		vet[i] = 0
	elif vet[i] != 9:
		vet[i] = vet[i] + 1
print(vet)