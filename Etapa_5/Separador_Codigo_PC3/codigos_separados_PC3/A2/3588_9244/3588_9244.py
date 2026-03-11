from numpy import*
vetor = array(eval(input("digite: ")))
ponto = 10000
i = 0

while (i < size(vetor)):
	if (vetor[i] == 1):
		ponto = ponto*2
	elif(vetor[i] == 2):
		ponto = ponto
	elif(vetor[i] == 3):
		ponto = ponto/2
	else:
		ponto = ponto/4
	i += 1
print(round(ponto, 2))