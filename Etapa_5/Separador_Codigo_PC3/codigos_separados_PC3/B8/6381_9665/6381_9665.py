from numpy import * 

carta = input("Digite o caractere da carta: ").upper().split(',')

cont = zeros(4,dtype=int)

for x in range(size(carta)): 
	if carta[x] == 'C':
		cont[0] = cont[0] + 1
	elif carta[x] == 'O':
		cont[1] = cont[1] + 1
	elif carta[x] == 'P':
		cont[2] = cont[2] + 1
	elif carta[x] == 'E':
		cont[3] = cont[3] + 1

print(cont)