from numpy import*
vetor = array(eval(input(" ")))

for i in range(size(vetor)):
	if (vetor[i] == 0):
		vetor[i] = 0
	else:
		vetor[i] *= 2
print(vetor)