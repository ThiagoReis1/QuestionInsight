from numpy import*

cont = zeros(6, dtype = int)

vet = input("Tipos de pele: ").upper().split(',')

for i in range(size(vet)):
	if (vet[i] == 'MC'):
		cont[0] = cont[0] + 1
	elif (vet[i] == 'C'):
		cont[1] = cont[1] + 1
	elif (vet[i] == 'CM'):
		cont[2] = cont[2] + 1
	elif (vet[i] == 'EM'):
		cont[3] = cont[3] + 1
	elif (vet[i] == 'E'):
		cont[4] = cont[4] + 1
	elif (vet[i] == 'ME'):
		cont[5] = cont[5] + 1
i = cont[0]
for i in range(1, size(cont)):
	if (i == max(cont)):
		print (i)
print(cont)
