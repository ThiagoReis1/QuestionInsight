from math import *
x= float(input('digite um valor para x: '))
eq= 0

if ((x<=-1) or (x>=1)):
	eq= sqrt(abs(x))
	print(round(eq, 2))
elif (((x>-1) and (x<0)) or ((x>0) and (x<1))):
	eq= abs(x)
	print(round(eq, 2))
else:
	(x==0)
	eq= 0
	print(eq)