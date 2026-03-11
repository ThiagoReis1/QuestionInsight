from numpy import *

produtos = input("Insira a categoria do produto: ").upper().split(',')
p = 0
vet = zeros(4, dtype=int)

for i in range(size(produtos)):
	if produtos[i] == "E":
		vet[0] +=  1
	elif produtos[i] == "V":
		vet[1] += 1
	elif produtos[i] == "A":
		vet[2] += 1
	elif produtos[i] == "D":
		vet[3] += 1
print(vet)

