from math import *
x = float(input("valor de x: "))
if x<=-1 or x>=1:
	total = x**2
	print(total)
elif -1<x<0 or 0<x<1:
	total = x
	print(total)
else:
	print(1)