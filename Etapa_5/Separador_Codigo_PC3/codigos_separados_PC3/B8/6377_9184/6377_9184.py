from numpy import *

gol = (input("Digite a sequencia de gols: ")).upper().split(',')

resultado = zeros(4, dtype = int)

for i in range (size(gol)):
	if gol[i] == 'A':
		resultado[0] += 1
		
	elif gol[i] == 'B':
		resultado[1] += 1
		
	elif gol[i] == 'C':
		resultado[2] += 1
		
	elif gol[i] == 'D':
		resultado[3] += 1
	
print(resultado)