from numpy import *
# Cria o vetor de 5 categorias com zeros
cont = zeros(5, dtype=int)
# Leitura do vetor de tipos NACIONALIDADES
vet = input("Tipos de NACIONALIDADE: ").upper().split(',')
# Contagem de NACIONALIDADES
for i in range(size(vet)):
	if (vet[i] == 'AR'):
		cont[0] = cont[0] + 1
	elif(vet[i] == 'BR'):
		cont[1] =cont[1] + 1
	elif(vet[i] == 'CL'):
		cont[2] = cont[2] + 1
	elif(vet[i] == 'CO'):
		cont[3] = cont[3] + 1
	elif(vet[i] == 'UY'):
		cont[4] = cont[4] + 1
print (cont)
for i in range(size(vet)):
	if (vet[i] % 2 == 2):
		vet= vet + 1
		print(vet)

	
		