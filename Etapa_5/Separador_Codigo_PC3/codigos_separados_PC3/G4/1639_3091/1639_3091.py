from numpy import*
v=array(eval(input("quantidade de alunos matriculados: ")))
par=0
for i in arange(size(v)):
	if v[i]%2==0:
		par=par+1
cop=zeros(par, dtype=int)
j=0
for i in arange(size(v)):
	if v[i]%2==0: # contagem para 
		cop[j]=i
		j=j+1
print(par)
print(cop)