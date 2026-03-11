from numpy import *
# Cria o vetor de 5 categorias com zeros
cont = zeros(5, dtype=int)

vet = input("").split(',')
# Contagem de ocorrencias
for x in vet:
	if (x == 'AZ'):
		cont[0] = cont[0] + 1
	elif (x == 'CA'):
		cont[1] = cont[1] + 1
	elif (x == 'FL'):
		cont[2] = cont[2] + 1
	elif (x == 'PA'):
		cont[3] = cont[3] + 1
	elif(x== 'WI'):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
	
