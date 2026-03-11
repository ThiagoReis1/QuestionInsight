from numpy import*
vetor = array(eval(input('Digite o vetor:')))
for i in range(size(vetor)):
	if vetor[i] == 9:
		vetor[i] = 0
	else:
	   vetor[i] = vetor[i] + 1
	
print(vetor)