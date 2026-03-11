from math import*

x = float(input("Informe o valor de x: "))

if(x<=-1 or x>=1):
	fx = abs(x ** (1/2))	
elif(x>-1 and x <0)or (0<x and x < 1):
	fx = abs(x)
else:
	fx = 0
print(round(fx,2))