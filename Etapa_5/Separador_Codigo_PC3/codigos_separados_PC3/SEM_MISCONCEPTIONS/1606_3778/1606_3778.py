from numpy import*
vetor = array(eval(input()))
i = 0
n = 0
while i < len(vetor)-1:
	if vetor[i] - vetor[i+1] >= 0:
		n = n + (vetor[i] - vetor[i+1])
	else:
		n = n + (vetor[i+1] - vetor[i])
	i = i + 1
print(n)