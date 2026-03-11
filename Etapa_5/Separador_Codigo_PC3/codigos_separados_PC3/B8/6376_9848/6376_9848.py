from numpy import *

pontos  = input("insira quantos pontos cada jogador marcou: ").upper().split(",")
jogadores = zeros (4, dtype=int)


for v in pontos:
	if v == "A":
		jogadores[0] += 1
	elif v == "B":
		jogadores[1] += 1
	elif v == "C":
		jogadores[2] += 1
	elif v == "D":
		jogadores[3] += 1
		
print(jogadores)