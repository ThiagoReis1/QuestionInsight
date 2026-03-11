from numpy import *

vetor = array(eval(input("Informe o vetor: ")))

i = 0
quantidade = 0
while (i < size(vetor)):
	if (-100 < vetor[i]):
		quantidade = quantidade + 1
	i = i + 1
vetor2 = zeros(quantidade, dtype=float)

i = 0
i2 = 0
while (i < size(vetor)):
	if (-100 < vetor[i]):
		vetor2[i2] = vetor[i]
		i2 = i2 + 1
	i = i + 1
	
print (vetor2)