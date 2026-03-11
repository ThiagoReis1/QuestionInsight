from math import*

x = float(input("valor de x: "))

if (0<x<=4):
	result1 = x**(1/2)
    
	print(round(result1, 4))
	
elif (-4<=x<0):
	result2 = abs(x**(1/2))
	print(round(result2, 4))
	
	

	
