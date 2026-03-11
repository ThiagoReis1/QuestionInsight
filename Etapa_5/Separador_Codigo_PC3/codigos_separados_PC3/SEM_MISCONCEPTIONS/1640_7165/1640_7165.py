from numpy import *
alunos = array(eval(input("quantidade de alunos matriculados em cada turma: ")))
q_impar = 0
for x in range(size(alunos)):
	if alunos[x] % 2 != 0:
		q_impar = q_impar + 1
print(q_impar)

aux = zeros(q_impar, dtype = int)

i = 0
for y in range(size(alunos)):
	if alunos[y] % 2 != 0:
		aux[i] = y
		i = i + 1
print(aux)
	