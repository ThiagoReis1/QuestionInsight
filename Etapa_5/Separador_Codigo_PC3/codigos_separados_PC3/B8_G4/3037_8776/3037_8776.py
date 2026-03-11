x = float(input())
if x <= -1 or x >= 1:
	print(x**2)
elif -1<x<0 or 0<x<1:
	print(x)
elif x==0:
	print(1)