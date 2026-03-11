from numpy import *

vetor = array(eval(input("Digite o vetor: ")))
i = 0
cont = 0
record = 307
while (i < size(vetor)):
	if (vetor[i] > 307):
		cont = cont + 1
		i = i + 1
	else:
		i = i + 1
print(record)
print(cont)
