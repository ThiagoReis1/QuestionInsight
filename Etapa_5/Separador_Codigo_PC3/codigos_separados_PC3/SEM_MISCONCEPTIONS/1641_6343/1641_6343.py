from numpy import *
qtd = array(eval(input("qtd: ")))
turmas = 0
for x in qtd:
	if (qtd % 3 == 0):
		turmas = turmas + 1
		print(turmas)