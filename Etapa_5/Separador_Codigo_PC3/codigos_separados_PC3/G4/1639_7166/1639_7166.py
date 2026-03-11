from numpy import*

v=array(eval(input("numero de alunos na turma: ")))
par=0
ind=[]
for i in range (size(v)):
	if(v[i]%2==0):
		par=par+1
		ind.append(i)
a=zeros(size(ind), dtype=int)
a=a+ind
print(par)
print(a)