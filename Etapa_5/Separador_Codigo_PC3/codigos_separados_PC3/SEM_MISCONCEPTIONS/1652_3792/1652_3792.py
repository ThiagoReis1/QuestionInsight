from numpy import*
cont = zeros(5, dtype=int)

sanguineos vet = input("quantidade de alunos: ").upper().split(',')

for i in range(size(vet)):
	if(vet[i] == 'B'):
	cont[0] = cont[0] + 1
	elif(vet[i] == 'PA'):
	cont[1] = cont[1] + 1
	elif(vet[i] == 'PR):
	cont[2] = cont[2] + 1
	elif(vet[i] == 'A'):
	cont[3] = cont[3] + 1
	elif(vet[i] == 'I'):
	cont[4] = cont[4] + 1
print(cont)