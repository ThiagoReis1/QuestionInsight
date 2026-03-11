from numpy import *

turmas = array(eval(input("Insira a quantidade de alunos: ")))
e = 0

for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		e += 1

ind = zeros(e, dtype=int)
print(e)

j = 0

for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		ind[j] = i
		j += 1

print(ind)