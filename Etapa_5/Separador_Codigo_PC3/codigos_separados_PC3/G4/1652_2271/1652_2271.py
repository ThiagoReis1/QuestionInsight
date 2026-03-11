from numpy import *
vet = input("quantidade de alunos: ").upper().split(',')
cont = zeros(5, dtype=int)
for i in range(size(vet)):
	if(vet[i] == "B"):
		cont[0] = cont[0] + 1
	if(vet[i] == "PA"):
		cont[1] = cont[1] + 1
	if(vet[i] == "PR"):
		cont[2] = cont[2] + 1
	if(vet[i] == "A"):
		cont[3] = cont[3] + 1
	if(vet[i] == "I"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)