

vetor = eval(input(" "))
i = 0
while vetor[0] > 0:
	from numpy import *
	if (vetor[i] == '1') or (vetor[i]  == '3') or (vetor[i] == '5'):
		pontuacao = 10
		i += 1
		pontuacao = i * pontuacao
	elif (vetor[i] == '2') or (vetor[i] == '4') or (vetor[i] == '6'):
		pontuacao = 5
		i += 1
		pontuacao = i * pontuacao
print(pontuacao)





