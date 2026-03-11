from numpy import *
pontuacao = 100
pontos = array(eval(input()))
for x in pontos:
	if x == 1:
		pontuacao *= 5
	elif x == 2:
		pontuacao *= 3
	elif x == 3:
		pontuacao += 0
	else:
		pontuacao /= 2
print(round(pontuacao,2))