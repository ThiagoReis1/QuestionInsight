import math

var = float(input())

if 0 <= var < 90 or 180 <= var < 270:
	calc = math.radians(var)
	calc0 = math.sin(calc)
	print(round(calc0,4))
elif 90 <= var < 180 or 270 <= var < 360:
	calc = math.radians(var)
	calc0 = math.cos(calc)
	print(round(calc0,4))
else:
	print("entrada invalida")