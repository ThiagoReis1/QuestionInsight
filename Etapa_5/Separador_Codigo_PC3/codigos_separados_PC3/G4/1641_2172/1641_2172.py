from numpy import *
a=array(eval(input("alunos matriculados:")))

n=0

for i in arange(0,size(a)):
	if(a[i]%(3)==0):
		n=n+1
print(n)
cont=zeros(n,dtype=int)
s=0

for i in arange(0,size(a)):
	if(a[i]%(3)==0):
		cont[s]=i
		s=s+1
print(cont)
		