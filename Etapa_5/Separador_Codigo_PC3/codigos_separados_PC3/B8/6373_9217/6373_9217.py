from numpy import *

tarefas = input("Digite os caracteres: ").split(",")

count = zeros(4,dtype = int)

for i in range(size(tarefas)):
	if tarefas[i] == "A":
		count[0] = count[0] + 1
	elif tarefas[i] == "P":
		count[1] = count[1] + 1
	elif tarefas[i] == "D":
		count[2] = count[2] + 1
	elif tarefas[i] == "M":
		count[3] = count[3] + 1
		
print(count)