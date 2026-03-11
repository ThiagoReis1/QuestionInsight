from numpy import *

#Numero de alunos
alunos = array(eval(input("Numero de alunos por turma: ")))

#Acumuladora do divisiveis por cinco
divisiveis = 0

#Contador de quantas turmas sao divisiveis por cinco
j = 0

for i in range(size(alunos)):
	if(alunos[i] % 5 == 0):
		divisiveis = divisiveis + 1
#Criar o vetor de divisiveis
p = zeros(divisiveis, dtype = int)

for i in range(size(alunos)):
	if(alunos[i] % 5 == 0):
		p[j] = i
		j = j + 1
print(divisiveis)
print(p)