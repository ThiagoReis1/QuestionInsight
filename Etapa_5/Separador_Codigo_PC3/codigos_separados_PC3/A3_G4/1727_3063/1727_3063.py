from numpy import*
from numpy .linalg import*

vet = array(eval(input("digite o vetor: ")))

lin = shape(vet)[0]
col = shape(vet)[1]

soma = zeros(2,dtype,float)

soma = 0

for i in range(lin):
	for j in range(col):
		soma[i] + vet[i,j]

print(max(vet))
