from numpy import *

vet = array(eval(input("Entre com um vetor: ")))
turma_5 = 0

for i in range(size(vet)):
	if vet[i] % 5 == 0:
		turma_5 = turma_5 + 1
print(turma_5)
		
cont = zeros(turma_5,dtype=int)
j = 0

for i in range(size(vet)):
	if vet[i] % 5 == 0:
		cont[j] = i
		j = j + 1
print(cont)
		