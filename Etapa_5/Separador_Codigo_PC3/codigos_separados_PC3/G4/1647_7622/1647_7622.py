from numpy import *

vet = array(eval(input("vetor de porcentagem de aulas frequentadas: ")))

ap = 0

for i in range(size(vet)):
	if vet[i] >= 70:
		ap += 1

vet_cont = zeros(ap, dtype = int)
j = 0

for i in range(size(vet)):
	if vet[i] >= 70:
		vet_cont[j] = i
		j += 1
print(ap)
print(vet_cont)