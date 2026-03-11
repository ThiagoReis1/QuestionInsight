from numpy import *

vetor = array(eval(input("Entre com a temperatura: ")))

i = 0
k = 0
while (i < size(vetor)):
	if (vetor[i] <= 40):
		k = k + 1
		i = i + 1
	else:
		i = i + 1

vetor1 = array(zeros(k , dtype = float))
j = 0
i = 0
while(i < size(vetor)):
	if (vetor[i]<= 40):
		vetor1[j] = vetor[i]
		j = j + 1
		i = i + 1
	else:
		i = i + 1
print(vetor1)