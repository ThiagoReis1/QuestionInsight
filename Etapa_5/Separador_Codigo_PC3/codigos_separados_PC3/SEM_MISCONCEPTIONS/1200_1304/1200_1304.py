from numpy import *
vetor = array(eval(input("vetor: ")))
i = 0
n = 0
while ( i < size(vetor)):
	if ( vetor[i] >= 0):
		n = n + 1
	i = i + 1
vetor2 = array(zeros(n, dtype = float))
i = 0
j = 0
while(i < size(vetor)):
	if ( vetor[i] >= 0):
		vetor2[j] = vetor[i]
		j = j + 1
	i = i + 1
print(vetor2)