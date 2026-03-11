def contar_tarefas(conclusoes):
	categorias = {'A': 0, 'P':1, 'D': 2, 'M': 3}
	contagem = [0, 0, 0, 0]
	
	tarefas = conclusoes.split(',')
	for tarefas in tarefas:
	   categoria = tarefa.strip()
	if categoria in categorias:
	   contagem[categorias[categoria]] += 1
	else:
			print(categoria)
	return contagem

conclusoes = input("Digite as tarefas concluidas:")
contagem = contar_tarefas(conclusoes)

print("tarefas administrativas concluidas", contagem[0])
print("tarefas de producao concluidas", contagem[1])
print("tarefas de desenvolvimento concluidas", contagem[2])
print("tarefas de markenting concluidas", contagem[3])
	