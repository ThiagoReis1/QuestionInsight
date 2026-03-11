from numpy import *

vetor = array(eval(input()))
i = 0
pontos = 0

while i < size(vetor):
	if vetor[i] == 1:
		pontos += 10
		
	elif vetor[i] == 2:
		pontos += 5
		
	elif vetor[i] == 3:
		pontos += 0
		
	elif vetor[i] == 4:
		pontos += 5
		
	elif vetor[i] == 5:
		pontos += 20
		
	elif vetor[i] == 6:
		pontos += 10
		
	i += 1
print(pontos)
		