from numpy import *

cartas = input("digite: ").split(",")
contagem = zeros(4, dtype=int)

for i in cartas:
	if (i == 'C'):
		contagem[0] += 1
	elif (i == 'O'):
		contagem[1] += 1
	elif (i == 'P'):
		contagem[2] += 1
	elif (i == 'E'):
		contagem[3] +=1	

print(contagem)