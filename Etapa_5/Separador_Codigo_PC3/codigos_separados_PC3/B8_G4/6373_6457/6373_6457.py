from numpy import *

c = input("Digite: ").upper().split(",")

vet = zeros(4, dtype=int)

for x in c:
	if x == "A":
		vet[0] = vet[0] + 1
	elif x == "P":
		vet[1] = vet[1] + 1 
	elif x == "D":
		vet[2] = vet[2] + 1
	elif x == "M":
		vet[3] = vet[3] + 1
print(vet)