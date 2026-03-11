from numpy import *
vetor = array(eval(input("Digite o vetor: ")))
i = 0
q = 0
while(i < size(vetor)):
	if(vetor[i]>=0):
		q = q + 1
	i = i + 1
vetor2 = zeros(q, dtype=float)
i = 0 
i2 = 0
while(i < size(vetor)):
	if(vetor[i]>=0):
		vetor2[i2] = vetor[i]
		i2 = i2 + 1
	i = i+ 1
print(vetor2)