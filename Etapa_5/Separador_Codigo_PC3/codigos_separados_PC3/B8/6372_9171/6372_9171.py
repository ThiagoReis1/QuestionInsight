from numpy import *
produto = input().upper().split(',')
vet = zeros(4, dtype = int)

for i in produto:
	if i == 'A':
		vet[0] += 1
	elif i == 'B':
		vet[1] += 1
	elif i == 'L':
		vet[2] += 1
	elif i == 'H':
		vet[3] += 1
		
print(vet)
		