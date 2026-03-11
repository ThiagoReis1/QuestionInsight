from numpy import *

jogadores = input("insira a sequencia de jogadores: ").upper().split(",")
jp = zeros(4, dtype=int)

for i in jogadores:
	if	i == "A":
		jp[0] += 1
	elif	i == "B":
		jp[1] += 1
	elif	i == "C":
		jp[2] += 1
	elif	i == "D":
		jp[3] += 1
		
print(jp)