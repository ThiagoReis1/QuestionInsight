from math import sqrt
x = float(input())

if(x<=-1 or x>=1):
	fx1= abs(x)
	fx = float(sqrt(fx1))
	print(round(fx, 2))
elif(-1<x<0 or 0<x<1):
	fx = abs (x)
	print(round(fx, 2))
else:
	print(0)