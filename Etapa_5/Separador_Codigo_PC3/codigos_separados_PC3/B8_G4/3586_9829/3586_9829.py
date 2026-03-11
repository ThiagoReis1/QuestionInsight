from numpy import *

vetor = array(eval(input("Insira pontuacao: ")))
acum = 0
i = 0
maxi = size(vetor)

while i < maxi:
	if vetor[i] == 1:
		acum += 100
	elif vetor[i] == 2:
		acum += 60
	elif vetor[i] == 3:
		acum += 20
	i += 1
print(acum)