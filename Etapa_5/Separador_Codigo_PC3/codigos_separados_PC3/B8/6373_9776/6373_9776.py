from numpy import*

def contar_tarefas(tarefas):
	contagem = [0,0,0,0]
	
	lista_tarefas = tarefas.split(',')
	
	for tarefa in lista_tarefas:
		if tarefa == "A":
			contagem[0] += 1
		elif tarefa == "P":
			contagem[1] += 1 
		elif tarefa == "D":
			contagem[2] += 1 
		elif tarefa == "M":
			contagem[3] += 1 
			
	return array(contagem)

entrada = input()
resultado = contar_tarefas(entrada)

print(resultado)