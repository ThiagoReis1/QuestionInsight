from numpy import *

alunos = array(eval(input("Insira a quantidade de alunos: ")))
trio = 0

for i in range(size(alunos)):
	if alunos[i] % 3 == 0:
		trio += 1
		
indice = zeros(trio, dtype=int)
print(trio)

j = 0

for i in range(size(alunos)):
	if alunos[i] % 3 == 0:
		indice[j] = i
		j += 1
print(indice)