from numpy import *
p=float(input())
x=array(eval(input()))
y=array(eval(input()))
t=p/(p+1)
v=(2*x+3*y)
f=0
for i in range (0,size(x)):
	f=abs(v[i])**t + f
n=(f)**t
print(n)
	