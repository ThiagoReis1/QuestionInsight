from numpy import *

vetor = array(eval(input("Valores: ")))

i = 0
soma = sum(vetor)

while(size(vetor) != i):
	if(vetor[i] >= 80):
		soma = soma - vetor[i] * 0.15
	else:
		soma =soma
	i = i + 1
print(round(soma,2))		