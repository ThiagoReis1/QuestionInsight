from numpy import *
vet = array(eval(input("Vetor: ")))
nimp=0
for i in range(size(vet)):
	if (vet[i] % 2 != 0):
		nimp = nimp + 1
print(nimp)

cont = zeros(nimp, dtype=int)
x = 0
for i in range(size(vet)):
	if (vet[i] % 2 != 0):
		cont[x] = i
		x  = x + 1
print(cont)