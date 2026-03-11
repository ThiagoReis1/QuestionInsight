from numpy import*
cont = zeros(4, dtype=int)

vet = (input("Digite os naipes das cartas: ")).upper().split(',')

for x in range(size(vet)):
	if( vet[x] == 'C'):
		cont[0] = cont[0] + 1
	elif( vet[x] == 'O'):
		cont[1] = cont[1] + 1
	elif( vet[x] == 'P'):
		cont[2] = cont[2] + 1
	elif( vet[x] == 'E'):
		cont[3] = cont[3] + 1
print(cont)
	