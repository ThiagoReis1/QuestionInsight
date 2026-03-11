from numpy import*
vetor=array(eval(input("digite a qntd de alunos:  ")))
turma=0 
for i in vetor:
	if i%5==0:
		turma=turma+1
print(turma)
cont=zeros(turma, dtype=int)
j=0
for i in range(size(vetor)):
	if vetor[i]%5==0:
		cont[j]=i
		j=j+1
print(con)
	
		