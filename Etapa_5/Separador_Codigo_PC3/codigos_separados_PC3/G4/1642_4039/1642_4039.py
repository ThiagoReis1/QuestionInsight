from numpy import *

vet = array(eval(input()))
h=0
g = 0
for elemento in vet:
	if(elemento % 5 == 0):
		g = g + 1

for elemento in range(0, size(vet)):
	if(vet[elemento] % 5 == 0):
		v=zeros(h, dtype=int)
		h = h + vet[elemento]

print(g)

print(v)
		