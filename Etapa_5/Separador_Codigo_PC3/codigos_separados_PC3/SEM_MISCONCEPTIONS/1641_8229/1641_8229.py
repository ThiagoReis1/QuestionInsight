import numpy as np 

def contar_turmas_trios(alunos):
	turmas_trios = 0 
	indices_turmas_trios = []
	
	for i, num_alunos in enumerate(alunos):
		if num_alunos % 3 == 0:
			turmas_trios += 1 
			indices_turmas_trios.append(i)
	return turmas_trios, np.array(indices_turmas_trios)

entrada = [18, 22, 21, 23, 24, 26]
turmas, indices = contar_turmas_trios(entrada)
print(turmas)
print(indices)