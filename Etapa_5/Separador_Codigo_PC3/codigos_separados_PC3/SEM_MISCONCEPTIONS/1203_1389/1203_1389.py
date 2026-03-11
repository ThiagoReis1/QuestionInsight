from numpy import*
vetor = array(eval(input()))
i = 0
qtd = 0
while (i < size(vetor)):
	if (vetor[i] > 2.5):
		qtd = qtd + 1
	i = i + 1
	
print("2.5")
print(qtd)