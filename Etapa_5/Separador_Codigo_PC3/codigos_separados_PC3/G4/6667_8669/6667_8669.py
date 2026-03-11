from numpy import *

vet= zeros(10,dtype=float)

for i in range(10):
	n= float(input("n: "))
	if n >= 0 and n <= 10:
		vet[i] = n

nmin= float(input("nota minima: "))

cont = 0
for i in range(size(vet)):
	if vet[i] >= (nmin):
		cont+= 1

vet2= zeros(size(cont),dtype=float)
a= 0

for i in range(size(vet2)):
	if vet[i] >= (nmin):
		cont= a
print

	
	