from numpy import *

vet_jogada = array(eval(input(": ")))
pontos = 10000

for jogada in vet_jogadas:
	if jogada == 1:
		pontos = pontos * 2 
	elif jogada == 2:
		continue
	elif jogada == 3:
		pontos = pontos  / 2
	elif jogada == 4:
		pontos = pontos / 4
		
print(round(pontos, 2))
	