from numpy import*
vetor= array(eval(input()))
i = 0
while (i < size(vetor)):
	if vetor[i] >= 80.0:
		vetor[i] = vetor[i] - 5.0
	i += 1
print(round(sum(vetor), 2))