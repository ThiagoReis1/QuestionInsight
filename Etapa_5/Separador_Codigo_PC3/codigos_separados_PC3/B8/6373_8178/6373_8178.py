from numpy import*

tarefas = input().upper().split(",")
contagem = zeros(4, dtype=int)

for tarefas in tarefas:
	if tarefas == "A":
		contagem[0] += 1
	elif tarefas == "P":
		contagem[1] += 1
	elif tarefas == "D":
		contagem[2] += 1
	elif tarefas == "M":
		contagem[3] += 1
	
print(contagem)
		
		
	