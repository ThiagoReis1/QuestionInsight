from numpy import *

vetor = eval(input(""))
soma = 0
i = 0
for i in range(0,len(vetor)):
	if(vetor[i] > 160.0):
		soma = soma + vetor[i] - 25.0
	else:
		soma = soma + vetor[i]
print(round(soma,2))
	