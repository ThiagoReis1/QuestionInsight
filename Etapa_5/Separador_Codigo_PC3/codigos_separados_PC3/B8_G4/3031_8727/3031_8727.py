from math import *

x= float(input("insira o valor:"))

if (x<=1):
	print(round(1 ,2))
elif (1<x)  and (x<=2):
	print(round(2 ,2))
elif (2<x ) and (x<=3):
	print(round(x**2,2))
elif (x>3):
	print(round(x**3,2))
 