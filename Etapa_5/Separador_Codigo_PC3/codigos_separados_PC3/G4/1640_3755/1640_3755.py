from numpy import *
n=array(eval(input('Numero de alunos:')))
z=zeros(size(n),dtype=int)
for i in range(size(n)):
	if n[i]%2!=0:
		z[0]=z[0]+1
print(z[0])
x=zeros(z[0],dtype=int)
l=0
for t in range(size(n)):
	if n[t]%2!=0:
		x[l]=x[l]+t
		l=l+1
print(x)