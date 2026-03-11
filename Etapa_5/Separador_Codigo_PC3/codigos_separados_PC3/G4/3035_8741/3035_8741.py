from math import *

x = float(input("entrada de x: "))

if x >= 0 and x < 360:
	if (0 <= x < 90) or (180 <= x < 270):
		seno = sin(radians(x))
		print(round(seno, 4))
	if (90 <= x < 180) or (270 <= x < 360):
		cos = cos(radians(x))
		print(round(cos, 4))
else:
	print("entrada invalida")