from numpy import *
a=array(eval(input("Tempo dos banhos:")))*5
b=array(eval(input("Per de agua:")))/100
c=size(a)
d=zeros(c,dtype=float)
x=0
while(x<c):
	d[x]=a[x]*b[x]
	x=x+1
print(round(sum(d),2))