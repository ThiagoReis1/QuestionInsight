from numpy import *

vet = array(eval(input()),dtype=int)

cont = 0

for i in range(size(vet)):
	if vet[i] % 5 == 0:
		cont += 1
		
vet2 = zeros(cont,dtype=int)
j = 0

for i in range(size(vet)):
	if vet[i] % 5 == 0:
		vet2[j] = i
		j += 1

print(cont)
print(vet2)