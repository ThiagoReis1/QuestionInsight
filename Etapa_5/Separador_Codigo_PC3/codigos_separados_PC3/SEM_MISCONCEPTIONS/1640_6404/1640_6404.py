from numpy import *

vet = eval(input(": "))
nimp = 0
count = 0

for elemento in vet:
	if elemento % 2 != 0:
		nimp += 1
vetzeros = zeros(nimp, dtype=int)

for i in range(size(vet)):
	if vet[i] % 2 != 0:
		vetzeros[count] += i 
		count += 1
print(nimp)
print(vetzeros)