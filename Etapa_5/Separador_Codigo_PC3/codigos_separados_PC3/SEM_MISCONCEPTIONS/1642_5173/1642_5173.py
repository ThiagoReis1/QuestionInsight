from numpy import * 

alunos = array(eval(input("entre com numero de alunos matriculados : ")))

cont = 0 

for i in range(size(alunos)):
	if alunos[i] %5 == 0:
		cont += 1
	
print(cont)
grupo = zeros(cont,dtype=int)

j = 0

for i in range(size(alunos)):
	if alunos[i] %5 == 0:	
		grupo[j] = i
		j += 1
print(grupo)
		
		
		
		
		
#numeros resto da divisao por 5 tem q dar 0 
#objt = contar e listar turmas de 5 alunos 