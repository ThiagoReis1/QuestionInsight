from numpy import*
from math import*
p=eval(input("p:"))
x=array(eval(input("x:")))
y=array(eval(input("y:")))
a=p+1
t=p/a
soma=0
for i in x:
	soma=soma+abs(i)**t
nx=(soma)**1/t
total=0
for j in y:
	total=total+abs(j)**t
ny=(total)**1/t
novo=x+y
f=0
g=0
k=x[f]*nx+y[g]*y
somatoria=0
for k in novo:
	somatoria=somatoria+abs(k)**t
	f=f+1
	g=g+1
	k=x[f]*nx+y[g]*y
nnovo=(somatoria)**1/t
print(round(nnovo,3))
	