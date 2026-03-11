from numpy import *

vet1 = array(eval(input("vetor: ")))
y=0
ap = 0
f = 0
for x in range(size(vet1)):
	if(vet1[x] >= 70 ):
		ap += 1
		
z = ap
vet2 = zeros(z, dtype = int)
for y in range(size(vet1)):
	if(vet1[y]>= 70):
		vet2[f] = y
		f += 1

print(ap)
print(vet2)