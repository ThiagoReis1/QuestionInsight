from math import *

x = float(input("insira o valor: "))

ans = 0.

if 0 <= x < 90 or 180 <= x < 270: 
	ans = sin(radians(x))
	print(round(ans, 4))
elif 90 <= x < 180 or 270 <= x < 360:
	ans = cos(radians(x))
	print(round(ans, 4))
elif x < 0:
	print('entrada invalida')