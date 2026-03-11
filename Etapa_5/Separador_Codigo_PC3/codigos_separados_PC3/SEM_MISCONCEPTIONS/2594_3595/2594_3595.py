from numpy import *

vetor = array(eval(input()))
qtdCritica = vetor[0]
cont = 0

for i in range(1,size(vetor)):
	if vetor[i] > qtdCritica:
		print(i)
		cont+=1

print(cont)