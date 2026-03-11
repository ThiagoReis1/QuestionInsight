from numpy import*
cont = zeros(5, dtype=int)
# Leitura do vetor de tipos sanguineos
vet = input("estados: ").upper().split(',')
for i in range(size(vet)):
	if(vet[i] == 'AR'):
		cont[0] += 1
	elif(vet[i] == 'BR'):
		cont[1] += 1
	elif(vet[i] == 'CL'):
		cont[2] += 1
	elif(vet[i] == 'CO'):
		cont[3] += 1
	elif(vet[i] == 'UY'):
		cont[4] += 1
print(max(cont))
print(cont)