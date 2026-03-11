from numpy import * 
p= float(input(""))
x=array(eval(input("")))
y=array(eval(input("")))
num=0
V=0
Z=0
a=zeros(size(x),dtype=float)
t=p/(p-1)
for c in range(size(x)):
	a[c]=(2*x[c])+(3*y[c])
for i in range (size(x)):
	A=abs(a[i])**t
	V+=A
	v=(V)**(1/t)
print(round(v,3))
