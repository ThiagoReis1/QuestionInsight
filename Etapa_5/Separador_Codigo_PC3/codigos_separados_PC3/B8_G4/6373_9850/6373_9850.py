from numpy import*

vet = input("Tarefas: ").upper().split(',')

cont = zeros(4, dtype=int)

for i in range(size(vet)):
	if(vet[i] == 'A'):
		cont[0] = cont[0] + 1
	elif(vet[i] == 'P'):
		cont[1] = cont[1] + 1
	elif(vet[i] == 'D'):
		cont[2] = cont[2] + 1
	elif(vet[i] == 'M'):
		cont[3] = cont[3] + 1
print(cont)
	