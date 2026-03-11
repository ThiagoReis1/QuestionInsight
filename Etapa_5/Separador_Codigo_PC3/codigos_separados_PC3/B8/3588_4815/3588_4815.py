from numpy import *
alvo = array(eval(input()))
i = 0
pontos = 10000
while i < size(alvo):
	if alvo[i] == 1:
		pontos *= 2
	elif alvo[i] == 3:
		pontos /= 2
	elif alvo[i] == 4:
		pontos /= 4
	i += 1
print(round(pontos, 2))