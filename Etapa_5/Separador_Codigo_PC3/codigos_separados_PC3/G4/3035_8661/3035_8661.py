from math import *

x= float(input())

if 0 <= x < 90 or 180 <= x < 270:
	y = radians(x)
	z = (sin(y))
	print(round(z, 4))
elif 90 <= x < 180 or 270 <= x < 360:
	y = radians(x)
	z = cos(y)
	print(round(z, 4))
else:
	print("entrada invalida")
