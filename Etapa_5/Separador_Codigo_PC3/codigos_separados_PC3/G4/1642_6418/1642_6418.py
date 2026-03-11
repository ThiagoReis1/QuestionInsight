from numpy import * 

A = array(eval(input()))

grupos = 0
for i in A:
	if i % 5 == 0:
		grupos += 1
print(grupos)

vet = zeros(grupos, dtype=int)
k=0
for i in range(size(A)):
	if A[i] % 5 == 0:
		vet[k] = i
		k = k + 1
print(vet)
		