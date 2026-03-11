from numpy import * 

pontos = input().split(',')

pontosPorJogador = zeros(4, dtype = int)

for jogador in pontos:
	if(jogador == 'A'):
		pontosPorJogador[0] += 1
	elif(jogador == 'B'):
		pontosPorJogador[1] += 1
	elif(jogador == 'C'):
		pontosPorJogador[2] += 1
	elif(jogador == 'D'):
		pontosPorJogador[3] += 1

print(pontosPorJogador)