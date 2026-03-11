from math import*

u = int(input())
v = int(input())
m = int(input())


t = 0

while( u > 0 and v > 0):
	
	u = u - v
	v = u - m 
 
	
	
	print(v)
	t = t + 1
