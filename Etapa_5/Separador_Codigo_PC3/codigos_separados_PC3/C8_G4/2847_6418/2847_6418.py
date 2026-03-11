from numpy import *

A = array(eval(input()))
vet = zeros(size(A),dtype=int)

k = 0
for i in A:
	i = i * i
	vet[k] = i
	k = k + 1
print(vet)