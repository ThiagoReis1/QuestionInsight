from numpy import *
votos = zeros(4, dtype = int)
candidatos = input("insira os candidatos: ").upper().split(',')
for i in range(size(candidatos)):
	if (candidatos[i] == 'A'):
		votos[0] = votos[0] + 1
	elif (candidatos[i] == 'B'):
		votos[1] = votos[1] +1
	elif (candidatos[i] == 'C'):
		votos[2] = votos[2] + 1
	elif (candidatos[i] == 'D'):
		votos[3] = votos[3] +1
		
print(votos)
