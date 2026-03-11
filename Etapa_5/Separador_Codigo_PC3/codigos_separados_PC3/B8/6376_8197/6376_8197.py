from numpy import *

cestas = input("Digite a sequencia de pontuadores: ").upper().split(',')
pontuadores = zeros(4, dtype=int)

for i in cestas:
	if (i == 'A'):
		pontuadores[0] = pontuadores[0] + 1
	elif (i == 'B'):
		pontuadores[1] = pontuadores[1] + 1
	elif (i == 'C'):
		pontuadores[2] = pontuadores[2] + 1
	elif (i == 'D'):
		pontuadores[3] = pontuadores[3] + 1
print(pontuadores)