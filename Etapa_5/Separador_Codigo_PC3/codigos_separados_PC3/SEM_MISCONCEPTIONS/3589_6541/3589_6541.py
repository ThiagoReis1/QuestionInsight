import numpy as np

vetor = np.array(eval(input()))

pontos = 0
i = 0
while i < len(vetor):
	if vetor[i] == 1:
		pontos+= 80
	elif vetor[i] == 2: 
		pontos += 40
	elif vetor[i] == 3:
		pontos+= 20
	else:
		pontos+=10
		
	i += 1
		
print(pontos)