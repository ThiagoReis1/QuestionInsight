from numpy import *

vet = array(eval(input('codigo: ')))
vet1 = zeros(size(vet), dtype=int)
vet2 = zeros(size(vet), dtype= int)
y = 0
for i in range(0, size(vet)):
	if vet[i] == 0:
		vet1[i] = 10
	elif vet[i] != 0:
		vet1[i]= vet[i]

for x in vet1:
	vet2[y] = x - 1
	y += 1
	
print(vet2)