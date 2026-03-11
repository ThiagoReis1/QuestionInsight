from numpy import * 

vetor = array(eval(input("Digite: ")))
i = 0
ponto = 0
while (i < size(vetor)):
	if (vetor[i] == 1):
		ponto = ponto + 10
	elif (vetor[i] == 2):
		ponto = ponto + 5
	elif (vetor[i] == 3):
		ponto = ponto + 0
	elif (vetor[i] == 4):
		ponto = ponto + 5
	elif (vetor[i] == 5):
		ponto = ponto + 20
	elif (vetor[i] == 6):
		ponto = ponto + 10
	i = i + 1
	
print(ponto)