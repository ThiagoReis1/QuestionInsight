from math import*
x = float(input("valor: "))

if x<=0:
	print(0)
elif 0<x<=1:
	print(1)
elif 1<x<=2:
	print(round(abs(x**(1/2)),4))
else:
	print(round(abs(x**(1/3)),4))