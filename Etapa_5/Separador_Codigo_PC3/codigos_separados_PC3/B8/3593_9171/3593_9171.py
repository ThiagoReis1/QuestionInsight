from numpy import *

vetor = array(eval(input()))

i = 0
pontos = 200

while i < size(vetor):
	if vetor[i] == 1 or vetor[i] == 3 or vetor[i] == 5:
		pontos = pontos / 2
	elif vetor[i] == 2 or vetor[i] == 4 or vetor[i] == 6:
		pontos = pontos * 3
	i += 1
print(round(pontos, 2))
	
	
	