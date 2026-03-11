from math import*

x = float(input("valor de x: "))
if (x<=0):
	f = 0
	print(round(f, 4))
elif ((0<x) and (x<=1)):
	f = 1
	print(round(f, 4))
elif ((1<x) and (x<=2)):
	f = x**(1/2)
	a = abs(f)
	print(round(a, 4))
elif (x>2):
	f = x**(1/3)
	a = abs(f)
	print(round(a, 4))	
	
	



	
	