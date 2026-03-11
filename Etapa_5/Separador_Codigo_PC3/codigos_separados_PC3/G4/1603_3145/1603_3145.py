from numpy import *
pt=[0,80,40,20,0]
vec=array(eval(input()))
a=0
c=0
b=0
while b<4:
	c+=pt[b]
	b=vec[a]
	a+=1
print(c)