from numpy import *

vetor = zeros(4, dtype=int)
produtos = input().upper().split(',')

for i in range(0,size(produtos), 1):
	if produtos[i] == "E":
		vetor[0] = vetor[0] + 1
	if produtos[i] == "V":
		vetor[1] =  vetor[1] + 1
	if produtos[i] == "A":
		vetor[2] = vetor[2] + 1
	if produtos[i] == "D":
		vetor[3] = vetor[3] + 1
print(vetor)