from numpy import *

alunos = array(eval(input()))
acum = 0

for i in range(size(alunos)):
	if alunos[i] >= 70:
		acum += 1
print(acum)

aprovados = zeros(acum, dtype=int)
j = 0
for i in range(size(alunos)):
	if alunos[i] >= 70:
		aprovados[j] = i
		j += 1
print(aprovados)