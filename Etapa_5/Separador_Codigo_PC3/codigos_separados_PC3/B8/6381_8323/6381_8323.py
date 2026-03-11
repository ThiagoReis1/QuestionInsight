from numpy import *

vet = input().upper().split(',')

naipe = zeros(4, dtype = int)

for i in range (len(vet)):
	if vet[i] == "C":
		naipe[0] += 1
	elif vet[i] == "O":
		naipe[1] += 1
	elif vet[i] == "P":
		naipe[2] += 1
	elif vet[i] == "E":
		naipe[3] += 1
print(naipe)