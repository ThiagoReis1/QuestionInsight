from numpy import*
vetor = array(eval(input("")))
i = 0
for i in range(size(vetor)):
	while vetor[i] == 9:
		vetor[i] -= 10
	else:
		vetor[i] = vetor[i] + 1
print(vetor)
	