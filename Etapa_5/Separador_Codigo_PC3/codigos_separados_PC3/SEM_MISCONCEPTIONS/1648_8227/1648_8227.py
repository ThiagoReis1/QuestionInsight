import numpy as np

def alunos_reprovados(frequencia):
	num_alunos = len(frequencia)
	reprovados =[]
	contador_reprovados = 0
	
	for i in range(num_alunos):
		if frenquencia[i] < 70:
			reprovados.append(i)
			contador_reprovados += 1
			
	return contador_reprovados, np.array(reprov
		