from numpy import *
alunos = array(eval(input("Frequencia de alunos: ")))
cont = 0 

for i in range(0,size(alunos)):
	if alunos[i]<70:
		cont = cont + 1
		
vetor = zeros(cont, dtype=int)
rep = 0
for i in range(0,size(alunos)):
	if alunos[i]<70:
		vetor[rep] = i
		rep = rep+1
				  
print(cont)
print(vetor)