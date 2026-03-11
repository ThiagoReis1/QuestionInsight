from numpy import*
cont = zeros(5, dtype=int)

vet = input("Cor dos Olhos: ").upper().split(',')


for i in range(size(vet)):
	if (vet[i] == 'P'):
		cont[0] = cont[0] + 1
	if (vet[i] == 'C'):
		cont[1] = cont[1] + 1
	if (vet[i] == 'M'):
		cont[2] = cont[2] + 1
	if (vet[i] == 'V'):
		cont[3] = cont[3] + 1
	if (vet[i] == 'A'):
		cont[4] = cont[4] + 1
			
print(max(cont))
print(cont)

