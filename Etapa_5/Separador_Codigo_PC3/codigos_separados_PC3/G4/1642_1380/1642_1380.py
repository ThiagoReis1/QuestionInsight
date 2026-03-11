from numpy import *

vet = array(eval(input("Informe quantidade de alunos em cada turma: ")))
vet = vet % 5
cont = 0

for i in range(size(vet)):
	if(vet[i] == 0):
		cont += 1

saida = arange(cont)
j = 0

for i in range(size(vet)):
	if(vet[i] == 0):
		saida[j] = i
		j += 1
	
print(cont)
print(str(saida).replace(",", " "))

