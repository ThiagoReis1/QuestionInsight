from numpy import *
alunos=array(eval(input("")))
i=0
n=0

g=0
h=0
j=0
while(i<size(alunos)):
	for x in alunos:
		if (alunos[i]%3==0):
			n=n+1
			i=i+1
	i=i+1
print(n)
t=zeros(n,dtype=int)
while(g<size(alunos)):
	for x in alunos:
		if (alunos[g]%3==0):
			t[j]=g
			g=g+1
			j=j+1
	g=g+1
print(t)