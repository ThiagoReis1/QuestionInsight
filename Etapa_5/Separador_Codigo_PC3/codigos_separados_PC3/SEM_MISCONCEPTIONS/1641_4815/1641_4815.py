from numpy import *
alunos = array(eval(input()))
cont = 0
trios = zeros(0, dtype=int)
for i in range(size(alunos)):
	if alunos[i] % 3 == 0:
		cont += 1
		trios = append(trios, i)
print(cont)
print(trios)