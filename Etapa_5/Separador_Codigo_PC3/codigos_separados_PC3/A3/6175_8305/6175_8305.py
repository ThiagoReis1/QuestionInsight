from math import *

x = float(input())

total = 0


if (x >= -4 and x < 0):
	total = abs(x) ** (1 / 2)
	print(round(total, 4))
elif((x >= 0) and (x <= 4)):
	total = x **(1 /2)
	print(round(total,4))
else:
	total = 'entrada invalida'
	print(total)
