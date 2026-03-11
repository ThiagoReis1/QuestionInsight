from numpy import *
vet = zeros(10, dtype=float)
cont = 0

for i in range(10):
	n = float(input())
	if 0 <= n <= 20:
		vet[i] = n
minimo = float(input())		
for i in range(10):
	if vet[i] >= minimo: 
		cont += 1
print(cont)	
vet = zeros(cont, dtype=float)

for 

		
		
		