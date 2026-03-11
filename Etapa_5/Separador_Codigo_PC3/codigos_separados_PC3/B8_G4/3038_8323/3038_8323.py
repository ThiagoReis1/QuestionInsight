from math import *

x = float(input("valor de x: "))

if (x <= -1 or x >= 1):
	x = abs(x)**(1/2)
	print(round(x, 2))
elif (x > -1 and x < 0) or (x > 0 and x < 1):
	x = abs(x)
	print(round(x, 2))
elif (x == 0):
	x = 0
	print(x)