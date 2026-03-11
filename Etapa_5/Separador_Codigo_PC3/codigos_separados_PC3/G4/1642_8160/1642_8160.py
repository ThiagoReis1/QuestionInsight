from numpy import *
v=array(eval(input('numero: ')))

c=0
x=""
for n in v:
	if(n%5==0):
		c=c+1
		x=x+n
print(c)
print(x)