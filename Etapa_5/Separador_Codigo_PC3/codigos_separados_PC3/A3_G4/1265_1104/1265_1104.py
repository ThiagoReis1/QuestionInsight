from numpy import*
from math import*
n=float(input())
x=array(eval(input()))
y=array(eval(input()))
t=n/(n-1)
i=0
sxy=0
while (i<size(x)):
	mx=abs(x[i])
	nx=2*(mx**t)
	sx=sx+nx
	my=abs(y[i])
	ny=3*(my**t)
	
	mxy=(sx+sy)**(1/t)
	i=i+1
print(round(mxy,3))	
	
	