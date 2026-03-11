from numpy import *
acertos = array(eval(input("Acertos: ")))
pontos = 100
i = 0
while i < size(acertos):
	if acertos[i] == 1:
		pontos *=5
	elif acertos[i] == 2:
		pontos *=3
	elif acertos[i] == 3:
		pontos = pontos
	elif acertos [i] == 4:
		pontos *= 0.5
	i+=1
print(round(pontos, 2))