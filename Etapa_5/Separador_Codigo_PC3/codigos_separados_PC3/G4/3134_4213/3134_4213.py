from numpy import *
a=array(eval(input("Numeros:")))
n=size(a)
x=0
v=zeros(n,dtype=float)
while(x<n):
	v[x]=(a[x]**2)/n
	x=x+1
e=sum(v)**(1/2)
print(round(e,2))
	