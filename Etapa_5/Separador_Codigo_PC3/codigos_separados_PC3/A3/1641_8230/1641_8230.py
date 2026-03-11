from numpy import *

qtd_alunos = array(eval(input("informe os numeros: ")))
indice_trios = 0
turmas_trios = [ ]

for i in range(len(qtd_alunos)):
	if qtd_alunos[i] % 3 == 0:
		turmas_trios += 1
		
indice = 0

for i in range(len(qtd_alunos)):
	if qtd_alunos[i] % 3 == 0:
		indice_trios.append(i)
		indice += 1
print(turmas_trios, indice_trios)