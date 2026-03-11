from math import*
x = float(input("Digite o valor de x:"))
if (x<=-1)and(x>=1):
	fx = x**(1/2)
	print(round(fx,2))
if (x>0)and(x<1):
	fx = abs(x)
	print(round(fx,2))
if (x==0):
	fx = 0
	print(round(fx,2))
	