from math import*
x = float(input("valor: "))

if(x<=-1) or (x>=1):
	print(round(abs(x**(1/2)),2))
elif(-1<x<0) or (0<x<1):
	print(round(abs(x),2))
elif(x==0):
	print(0)