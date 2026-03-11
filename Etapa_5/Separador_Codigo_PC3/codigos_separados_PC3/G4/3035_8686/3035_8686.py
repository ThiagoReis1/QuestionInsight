from math import *

x = float(input("x: "))

if (0 <= x < 90) or (180 <= x < 270):
	x = radians(x)
	print(round(sin(x), 4))
elif (90 <= x < 180) or (270 <= x < 360):	
	x = radians(x)
	print(round(cos(x), 4))
else:
	print("entrada invalida")
