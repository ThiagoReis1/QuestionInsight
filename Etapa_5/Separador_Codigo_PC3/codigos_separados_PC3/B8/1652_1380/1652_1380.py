from numpy import *

alunos = input("Informe as etnias dos alunos: ").upper().split(",")

cont = zeros(5,dtype=int)

for i in range(size(alunos)):
	if (alunos[i] == 'B'):
		cont[0] += 1
	elif (alunos[i] == 'PA'):
		cont[1] += 1
	elif (alunos[i] == 'PR'):
		cont[2] += 1
	elif (alunos[i] == 'A'):
		cont[3] += 1
	elif (alunos[i] == 'I'):
		cont[4] += 1

maior = 0

for i in range(size(cont)):
	if (cont[i] > maior):
		maior = cont[i]

print(maior)
print(cont)