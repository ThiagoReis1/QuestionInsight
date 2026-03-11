from numpy import *
p=float (input())
x=array(eval(input()))
y=array(eval(input()))
t=p/(p-1)
s=0
for i in range (0,size(x)):
	s=s+ abs(2*x[i]+3*y[i])**t
d=(s)**(1/t)
print(round(d, 3))
