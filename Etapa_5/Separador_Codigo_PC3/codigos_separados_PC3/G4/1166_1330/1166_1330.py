from math import *
n = int(input())
a = 1
b = 1
s = 0 
while (n>0):
	if(n%2==0):
		s = a**0.5/6+b + s
	else:
		s = -a**0.5/6+b + s
	a = a + 1
	b = b + 2
print (round(x,10))
	
