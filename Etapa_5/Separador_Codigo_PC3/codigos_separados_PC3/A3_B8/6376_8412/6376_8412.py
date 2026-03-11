from numpy import *
jogador = input("insira os jogadores: ").split(",")
vet = zeros(4, dtype = int)
cont = 0 

for ch in jogador:
	if ch == 'A':
		vet[0] += 1
	elif ch == 'B':
		vet[1] +=1
	elif ch == 'C':
		vet[2] += 1
	elif ch == 'D':
		vet[3] += 1
		
		
print(vet)
