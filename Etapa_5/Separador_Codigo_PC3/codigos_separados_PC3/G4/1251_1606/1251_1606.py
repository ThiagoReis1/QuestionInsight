from numpy import *
v=array(eval(input("Digite:")))
A=min(v)
B=max(v)
C=0.7*A+0.3*B
D=0.4*A+0.6*B
saida=zeros(2,dtype=int)
i=0
x1=0
x2=0
while (i<size(v)):
	if((v[i]>=A)and(v[i]<C)):
		x1= x1+1
	if((v[i]>=C)and(v[i]<D)):
		x2=x2+1
i=i+1
saida[0]=x1
saida[1]=x2
print(saida)