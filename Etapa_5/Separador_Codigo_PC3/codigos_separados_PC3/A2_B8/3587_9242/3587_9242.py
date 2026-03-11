from numpy import *
anel = array(eval(input('aneis: ')))
pontos = 100
i = 0
while (i < size(anel)):
	if(anel[i] == 1):
		pontos = pontos * 5
	elif(anel[i] == 2):
		pontos = pontos * 3
	elif(anel[i] == 3):
		pontos = pontos
	elif(anel[i] == 4):
		pontos = pontos / 2
	i += 1
print(round(pontos, 2))