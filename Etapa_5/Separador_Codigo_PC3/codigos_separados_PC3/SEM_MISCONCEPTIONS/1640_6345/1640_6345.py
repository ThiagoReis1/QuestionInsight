from numpy import *

vet = array(eval(input("digite um numero: ")))
nimpar = 0

for i in range(size(vet)):
	if vet[i] % 2 != 0:
		nimpar = nimpar + 1

zero = zeros(nimpar, dtype=int)

nindice = 0

for a in range(size(zero)):
	if vet[a] % 2 != 0:
		if vet[0] % 2 != 0:
			zero[0] = 0	
		
		nindice = nindice + 1
		zero[a] = zero[a] + nindice 

print (nimpar)
print (zero)