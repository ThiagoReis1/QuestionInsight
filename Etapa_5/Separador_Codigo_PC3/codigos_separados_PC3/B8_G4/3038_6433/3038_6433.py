from math import *

x = float(input("x: "))

if(x <= -1 or x>= 1):
	x = abs(x)**(1/2)
	
elif(-1<x<0 or 0<x<1):
	x = abs(x)
	
elif (x==0):
	x = 0
	
print(round(x, 2))