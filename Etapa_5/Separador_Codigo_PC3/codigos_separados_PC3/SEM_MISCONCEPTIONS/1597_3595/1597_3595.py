from numpy import *

vetor = array(eval(input()))
custo = 0

for i in range(size(vetor)):
	custo+=vetor[i]
	if(vetor[i]>80):
		custo-=5
		
print(round(custo, 2))