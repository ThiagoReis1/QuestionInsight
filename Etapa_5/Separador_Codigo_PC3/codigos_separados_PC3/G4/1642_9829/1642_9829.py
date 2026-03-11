from numpy import *

turma = array(eval(input("Digite o vetor com os alunos de cada turma: ")))

cont = 0
tam = size(turma)


for i in range(tam):
	if turma[i] % 5 == 0:
		cont += 1
print(cont)
zero = zeros(cont, dtype=int)
		
print(zero)