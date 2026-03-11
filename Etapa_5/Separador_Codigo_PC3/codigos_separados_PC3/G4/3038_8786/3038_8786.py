from math import*

x = float(input())


if -1>=x>=1:
	a = abs(x) ** (1/2)
	print(round(a, 2))
if -1<x<0 or 0<x<1:
	a = abs(x)
	print(round(a, 2))
if x == 0:
	print(x)