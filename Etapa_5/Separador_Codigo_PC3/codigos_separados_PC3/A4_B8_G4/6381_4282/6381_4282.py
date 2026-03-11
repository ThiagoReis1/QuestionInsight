from numpy import *
str = input().upper().split(',')

vet = zeros(4, dtype=int)
for char in str:
	if (char == 'C'):
		vet[0] += 1
	elif (char == 'O'):
		vet[1] += 1
	elif (char == 'P'):
		vet[2] += 1
	elif (char == 'E'):
		vet[3] += 1
print(vet)