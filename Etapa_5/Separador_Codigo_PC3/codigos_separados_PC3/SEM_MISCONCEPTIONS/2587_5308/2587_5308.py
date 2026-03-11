from numpy import*

vetor = array(eval(input(": ")))

limite = vetor[0] + vetor[0]/2

j = 0

for i in range(size(vetor)):
	if vetor[i] > limite:
		print(i)
		j = j + 1
		
	else:
		vetor[i] = vetor[i]
		
print(j)