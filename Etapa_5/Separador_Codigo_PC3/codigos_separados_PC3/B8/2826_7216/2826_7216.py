from numpy import*

notas_alunos = array(eval(input("")))
i = 0

while (i < size(notas_alunos)):
	if (notas_alunos[i] < 2):
		notas_alunos[i] = 0
	elif (notas_alunos[i]>8):
		notas_alunos[i] = 10
	
	i = i+1
print(notas_alunos)