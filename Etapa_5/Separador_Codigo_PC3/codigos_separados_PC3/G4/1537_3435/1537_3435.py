from math import *
x = float(input("x?"))
k = int(input("k?"))

t=1
s=0
f=2
g=1

while(f>0):
	b= factorial(t)
	a=x**t
	c=(-1)**(g+1)
	d=c*a/b
	s=s+d
	t=t+2
	g=g+1
	f=k-g+1
	
print(round(s,9))
