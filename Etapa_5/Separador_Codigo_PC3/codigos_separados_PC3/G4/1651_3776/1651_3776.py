from numpy import *
v=array(eval(input())).split('MC,C,CM,EM,E,ME')
t=0
y=0
c=0
while t<size(v):
	if v[t]=="MC":
		c=c+1
	t=t+1
t=0
x=zeros(c,dtype=int)
while t<size(v):
	if v[t] == 'C':
		x[y]=t
		y=y+1
	t=t+1
print(c)
print(x)
