from numpy import *

vet = zeros(10, dtype=float)

for i in range(10):
	n = float(input(''))
	if 0 <=n<= 10:
		vet[i] = n
min = float(input(''))

cont = 0

for i in vet:
	if i > min:
		cont += 1
print(cont)

vet2 = zeros(cont, dtype=float)

j = 0

for i in range(size(vet)):
	if vet[i] >= min:
		vet2[j] += vet[i]
		j += 1
print(vet2)
