from math import *

x = float(input('Digite um valor: '))

if (x >= 0 and x < 90) or (x >= 180 and x < 270):
	x = radians(x)
	y = sin(x)
	print(round(y, 4))
elif (x >= 90 and x < 180) or (x >= 270 and x < 360):
	x = radians(x)
	y = cos(x)
	print(round(y, 4))
else:
	print('entrada invalida')