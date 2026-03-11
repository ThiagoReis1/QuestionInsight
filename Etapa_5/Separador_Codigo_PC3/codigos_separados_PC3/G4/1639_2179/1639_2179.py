from numpy import *

turmas = array(eval(input("Quantidade de alunos matriculados: ")))
x = 0

for i in range(size(turmas)):
	if (turmas[i] % 2 == 0):
		x = x + 1
vet = zeros(x, dtype=int)

print(x)

y = 0

for i in range(size(turmas)):
	if (turmas[i] % 2 == 0):
		vet[y] = i
		y = y + 1
print (vet)