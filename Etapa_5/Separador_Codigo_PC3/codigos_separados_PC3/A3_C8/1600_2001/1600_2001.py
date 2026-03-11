from math import * 
from numpy import *
from numpy.linalg import *

vetor = array(eval(input("Digite os custos: ")))

i = 0
x = 0 

for i in range(size(vetor)):
	if vetor[i] > 80:
		vetor[i] = vetor[i] * 0,75
	else:
		vetor[i] = vetor[i]
	i = i + 1	

print (sum(vetor))
	