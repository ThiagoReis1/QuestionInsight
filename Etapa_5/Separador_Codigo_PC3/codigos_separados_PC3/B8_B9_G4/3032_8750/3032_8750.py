from math import*

x = float(input("valor de x: "))

if (x <= 0):
	f = 0
	print(round(f, 4))
elif (x > 0) and (x <= 1):
	f = 1
	print(round(f, 4))
elif (x > 1 ) and (x <= 2):
	f = x**(1/2)
	print(round(f, 4))
elif (x > 2):
	f = x**(1/3)
	print(round(f, 4))