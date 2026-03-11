from numpy import*
vetor = array(eval(input("")))

for i in range(size(vetor)):
	if (vetor[i] == 9 ):
		vetor[i] = 0
		v = (vetor + 1)**3
	else:
		v = (vetor + 1)**3
print(v)
		
	