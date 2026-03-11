from numpy import *

vet = array(eval(input()))
vet2 = array(eval(input()))
vet3 = zeros(size(vet),dtype=float)

j = 0
ap = 0

for i in vet:
	vet3[j] = vet[j] + vet2[j]
	if(vet3[j] >= 12):
		ap = ap + 1
	j = j + 1
	
print(vet3)
print(ap)
					
	