#Ingrid do Nascimento Mendes 11/08/2016
from numpy import *

vetor1 = array(eval(input()))
n = 0
i = 0
while (size(vetor1) > i):
	if (vetor1[i] > 0):
		n = n + 1
	i = i + 1

vetor2 = array(zeros(n,dtype=float))

i = 0
j = 0
while (size(vetor1) > i):
	if (vetor1[i] > 0):
		vetor2[j] = vetor1[i]
		j = j + 1
	i = i + 1
print (vetor2)