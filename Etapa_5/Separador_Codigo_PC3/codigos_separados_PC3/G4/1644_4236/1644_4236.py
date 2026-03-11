from numpy import*

vet = array(eval(input(" ")))
r = 0
for i in range(size(vet)):
	if (vet[i] < 5):
		r = r + 1
print(r)

vetor = zeros(r, dtype=int)
k = 0
j = 0
for i in range(size(vet)):
	if (vet[i] < 5):
		vetor[k] = vetor[k] + j
		k = k + 1
	j = j + 1
print(vetor)

		
	