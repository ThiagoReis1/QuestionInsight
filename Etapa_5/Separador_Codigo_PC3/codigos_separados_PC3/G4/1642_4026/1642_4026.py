from numpy import*
qtda=array(eval(input("Quantidade de alunos matriculados:")))
j=0
n=size(qtda)
for i in range(n):
	if(qtda[i] % 5 == 0):
		j=j+1
z=zeros(j,dtype=int)
k = 0
#Criacao do vetor das turmas
for i in range(n):
	if (qtda[i] % 5 == 0):
		z[k] = i
		k=k+1
print(j)
print(z)