from numpy import *

vet = input().upper().split(',')
vet1 = zeros(4, dtype=int)

for i in range(size(vet)):
	if vet[i] == 'A':
		vet1[0] += 1
	elif vet[i] == 'B':
		vet1[1] += 1
	elif vet[i] == 'C':
		vet1[2] += 1
	elif vet[i] == 'D':
		vet1[3] += 1
print(vet1)