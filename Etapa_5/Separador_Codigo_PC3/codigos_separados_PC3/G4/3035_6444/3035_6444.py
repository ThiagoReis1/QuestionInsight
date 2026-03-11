from math import *
x = float(input())

if 0 <= x < 360:
	if 0 <= x < 90 or 180 <= x < 270:
		print(round(sin(radians(x)), 4))
	else:
		print(round(cos(radians(x)), 4))
else:
	print('entrada invalida')