from numpy import *

vet = zeros(10, dtype=float)

for i in range(len(vet)):
	num = int(input())
	vet[i] = num

limite = int(input())	

contador = 0

for i in range(len(vet)):
	
	if vet[i] >= limite:
		contador = contador + 1
		
print(contador)

vet2 = zeros(contador, dtype=float)

for i in range(len(vet)):
	if vet[i] >= limite:
		vet2[i] = vet[i]

print(vet2)