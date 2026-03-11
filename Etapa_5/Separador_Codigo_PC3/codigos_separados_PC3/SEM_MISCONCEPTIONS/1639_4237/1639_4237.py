from numpy import * 

alunos = array(eval(input("Turmas: ")))
turmas = 0
j = 0

for i in range(size(alunos)):
	if(alunos[i]%2 == 0):
		turmas = turmas + 1 
		
total = zeros(turmas, dtype=int)

for i in range(size(alunos)):
	if(alunos[i]%2 == 0):
		total[j] = i
		j = j+1 
		
print(turmas)
print(total)