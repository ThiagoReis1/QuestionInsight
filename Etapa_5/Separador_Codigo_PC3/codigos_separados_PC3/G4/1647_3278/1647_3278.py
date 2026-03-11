from numpy import *
cont = zeros(5, dtype = int)
vet = input("notas dos alunos: ").upper().split(',')

for x in vet:
	if (x > '70'):
		cont[0] = cont[0] + 1

for x in vet:
	if (x == '70'):
		cont[0] = cont[0] + 1
	
print (sum(cont))			
print(cont)