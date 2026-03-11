from numpy import*
vetor = array(eval(input("digite o vetor: ")))
ponto_t = 100
i = 0

while(i < size(vetor)):
	if (vetor[i] == 1):
		ponto_t = ponto_t * 5
	elif (vetor[i] == 2):
		ponto_t = ponto_t * 3
	elif (vetor[i] == 3):
		ponto_t = ponto_t
	else:
		ponto_t = ponto_t/2
	i += 1
print(round(ponto_t, 2))