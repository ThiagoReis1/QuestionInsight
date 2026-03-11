from numpy import *

vet = array(eval(input("Digite a qt. de alunos em cada turma: ")))
cont = 0

for i in vet:
	if(i%5 == 0):
		cont += 1

indices = zeros(cont, dtype=int)

j = 0
for i in range(size(vet)):
	if(vet[i]%5 == 0):
		indices[j] = i
		j += 1

print(cont)
print(indices)