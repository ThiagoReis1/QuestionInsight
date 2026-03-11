from numpy import *

alunos = array(eval(input()))
cont = 0
for i in range(0,size(alunos)):
	if (alunos[i]%3==0):
		cont=cont+1

turmas = zeros(cont, dtype=int)

cont = 0
for i in range(0,size(alunos)):
	if (alunos[i]%3==0):
		turmas[cont]=i
		cont=cont+1
	
print(size(turmas))
print(turmas)