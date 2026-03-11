from numpy import *
acertos = array(eval(input("insira os acertos realizados: ")))
pontos = 10000
i = 0
while i < size(acertos):
	if acertos[i] == 1:
		pontos *= 2
	elif acertos[i] == 3:
		pontos /= 2
	elif acertos[i] == 4:
		pontos /= 4
	i += 1
print(round(pontos, 2))