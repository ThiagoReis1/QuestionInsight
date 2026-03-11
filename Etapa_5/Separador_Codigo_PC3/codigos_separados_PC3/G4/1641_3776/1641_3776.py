from numpy import *
v=array(eval(input()))
t=0
y=0
c=0
while t<size(v):
	if v[t]%3 == 0:
		c=c+1
	t=t+1
t=0
x=zeros(c,dtype=int)
while t<size(v):
	if v[t]%3 == 0:
		x[y]=t
		y=y+1
	t=t+1
print(c)
print(x)