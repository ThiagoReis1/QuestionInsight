from numpy import *
vet = zeros(10,dtype=float)
for i in range(10):
	n = float(input())
	if 0 <= n <= 10:
		vet[i] = n
print(size(vet))
print(vet)