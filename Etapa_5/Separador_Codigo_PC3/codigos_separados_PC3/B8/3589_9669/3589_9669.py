from numpy import *

acertos = array(eval(input("Entre com o local dos acertos: ")))

i = 0
pontos = 0

while i < size(acertos):
	if acertos[i] == 1:
		pontos = pontos + 80
	elif acertos[i] == 2:
		pontos = pontos + 40
	elif acertos[i] == 3:
		pontos = pontos + 20
	elif acertos[i] == 4:
		pontos = pontos + 10
	i = i + 1

print(pontos)
	