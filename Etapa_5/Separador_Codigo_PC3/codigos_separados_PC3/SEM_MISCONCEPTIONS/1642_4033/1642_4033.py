from numpy import*
from numpy.linalg import*

alunos=array(eval(input("Digite a quantidade de alunos por turma: ")))

cont=0
for i in range(size(alunos)):
	if(alunos[i]%5==0):
		cont=cont+1
		
print(cont)

possivel=zeros(cont,dtype=int)

k = 0
for j in range(size(alunos)):
	if(alunos[j]%5==0):
		possivel[k]=j
		k = k + 1
print(possivel)