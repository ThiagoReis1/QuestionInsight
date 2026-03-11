from numpy import *
a=array(eval(input("Ataques:")))
b=size(a)
x=0
m=1
at=ones(b,dtype=int)
while(x<b):
	a[x]=a[x]*m
	x=x+1
	m=m+1
print(sum(a))