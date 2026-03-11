from math import*
x = float(input(":"))
if (x<=0):
	f= abs(0)
	print(f)
elif (0<x) and (x<=1):
	f = abs(1)
	print(f)
elif (1<x) and (x<=2):
	f = abs(x**(1/2))
	print(round(f,4))
else:
	f = abs(x**(1/3))
	print(round(f,4))