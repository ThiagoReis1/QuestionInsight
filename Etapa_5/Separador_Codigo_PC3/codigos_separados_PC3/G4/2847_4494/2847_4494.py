from numpy import *

vet = eval(input())
vet2 = zeros(size(vet), dtype=int)

for i in range(0, size(vet)):
	vet2[i] = vet[i]**2
	
print(vet2)