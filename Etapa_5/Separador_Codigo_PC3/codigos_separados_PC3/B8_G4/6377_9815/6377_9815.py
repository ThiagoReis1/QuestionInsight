from numpy import *

gol = input("Insira os Jogadores: ").upper().split(",")
arm = zeros(4, dtype=int)

for i in range(size(gol)):
	if gol[i] == "A":
		arm[0] += 1
	elif gol[i] == "B":
		arm[1] += 1
	elif gol[i] == "C":
		arm[2] += 1
	elif gol[i] == "D":
		arm[3] += 1
		
print(arm)