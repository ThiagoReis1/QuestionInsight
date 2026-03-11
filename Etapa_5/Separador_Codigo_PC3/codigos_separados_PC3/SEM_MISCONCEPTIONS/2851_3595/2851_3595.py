from numpy import *

vetor = eval(input())
soma = 0

for indice in range(len(vetor)):
	if vetor[indice] == 99:
		soma*=2
	else:
		soma+=vetor[indice]
		
print(soma)