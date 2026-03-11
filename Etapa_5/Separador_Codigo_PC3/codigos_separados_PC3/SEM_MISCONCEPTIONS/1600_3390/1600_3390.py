from numpy import *

vetor = array(eval(input()))
n= size(vetor)
i=0
while n>i:
	if vetor[i] > 80.00:
		desconto= vetor[i] * 15/100
		vetor[i]= vetor[i] - desconto
		vetor[i]= round(vetor[i],2)
	else:
		vetor[i]= vetor[i]
		vetor[i]= round(vetor[i],2)
	i=i+1
vetor1= sum(vetor)
vetor1= round(vetor1,2)
print(vetor1)