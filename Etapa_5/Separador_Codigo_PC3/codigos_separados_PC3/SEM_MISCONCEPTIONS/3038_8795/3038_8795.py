from math import* 
x=float(input("funcao: "))
if x<=-1 or x>=1:
	x=(x**1/|x|)*abs()
	print(round(x, 2))
elif -1<x<0 or 0<x<1:
	x=|x|
	print(round(x, 2))
else:
	x=0
	print(x)