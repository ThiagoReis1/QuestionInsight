from numpy import *
jogadores = input().split(',')
resultado = zeros(4, dtype=int)
for jogador in jogadores:
	if jogador == 'A':
		resultado[0] += 1
	elif jogador == 'B':
		resultado[1] += 1
	elif jogador == 'C':
		resultado[2] += 1
	else:
		resultado[3] += 1
print(resultado)