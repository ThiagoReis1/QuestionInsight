from numpy import *
vetor = array(eval(input("Digite as pontuacoes: ")))
i = 0
total = 10000

while i < len(vetor):
	if vetor[i] == 1:
		total = total * 2
	elif vetor[i] == 2:
		total = total
	elif vetor[i] == 3:
		total = total / 2
	elif vetor[i] == 4:
		total = total /4
	i = i + 1
print(round(total, 2))