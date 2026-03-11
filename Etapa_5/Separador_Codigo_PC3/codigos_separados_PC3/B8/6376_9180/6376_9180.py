from numpy import*

jogador = input('Digite o caracter do jogador:').upper()

vet = zeros(4,dtype = int)

for i in range(len(jogador)):
	if jogador[i] == 'A':
		vet[0] = vet[0] + 1
	elif jogador[i] == 'B':
		vet[1] = vet[1] + 1
	elif jogador[i] == 'C':
		vet[2] = vet[2] + 1
	elif jogador[i] == 'D':
		vet[3] = vet[3] + 1
		
print(vet)		
		
		