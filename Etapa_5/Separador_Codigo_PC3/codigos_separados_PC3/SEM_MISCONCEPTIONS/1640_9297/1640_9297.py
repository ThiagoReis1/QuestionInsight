import numpy as np

def turmas_impares(alunos_por_turma):
	num_turmas_impares = 0
	indices_turmas_impares = []
	
	for i in range(len(alunos_por_turma)):
		if alunos_por_turma[i]%2! = 0:
		num_turmas_impares += 1
		indices_turmas_impares.append(i)
		
	return num_turmas_impares, indice_turmas_impares

alunos_por_turma = [20, 15, 23, 18, 25, 12, 17]

num_turmas_impares, indices_turmas_impares = turmas_impares(alunos_por_turma)

print(num_turmas_impares)
print(indice_turmas_impares)
