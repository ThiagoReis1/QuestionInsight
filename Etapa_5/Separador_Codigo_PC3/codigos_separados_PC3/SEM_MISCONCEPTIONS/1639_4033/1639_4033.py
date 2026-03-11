from numpy import*
from numpy.linalg import*

turma=array(eval(input("Digite a quantidade de alunos por cada turma: ")))

par=0

for i in range(size(turma)):
	if(turma[i]%2==0):
		par=par+1
		
print(par)
indices=zeros(par,dtype=int)

k=0
for j in range(size(turma)):
	if(turma[j]%2==0):
		indices[k]=j
		k=k+1
print(indices)
		