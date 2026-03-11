from numpy import *
dados = array(eval(input()))
pontos = 200
i = 0

while i < len(dados):
	if dados[i] == 1:
		pontos = pontos / 2
	elif dados[i] == 2:
		pontos = pontos * 3
	elif dados[i] == 3:
		pontos = pontos / 2
	elif dados[i] == 4:
		pontos = pontos * 3
	elif dados[i] == 5:
		pontos = pontos / 2
	elif dados[i] == 6:
		pontos = pontos * 3
	i = i +1

	
round2 = round(pontos, 2)
print(round2)