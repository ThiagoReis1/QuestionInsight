from numpy import *

vetor = array(eval(input()))

soma=0
for i in range(size(vetor)):
	if(vetor[i]!=88):
		soma=soma+vetor[i]
	else:
		soma = soma/2
	
print(soma)