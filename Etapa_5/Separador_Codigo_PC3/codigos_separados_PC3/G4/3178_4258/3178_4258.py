from numpy import *

vet = array(eval(input("Vetor: ")))
nvet = zeros(size(vet), dtype=int)
j = 0

for i in range(0, size(vet)):
	if(vet[i] != 0):
		nvet[j] =  vet[i]
		j = j + 1
print(nvet)