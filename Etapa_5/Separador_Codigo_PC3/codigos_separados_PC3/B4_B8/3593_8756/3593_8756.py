from numpy import *

dado = array(eval(input()))
pontos = 200
i = 0

while i < size(dado):
	if dado[i] == 1:
		pontos = pontos / 2
	elif dado[i] == 2:
		pontos = pontos * 3
	elif dado[i] == 3:
		pontos = pontos / 2
	elif dado[i] == 4:
		pontos = pontos * 3
	elif dado[i] == 5:
		pontos = pontos / 2
	elif dado[i] == 6:
		pontos = pontos * 3
	i = i + 1
print(round(pontos,2))