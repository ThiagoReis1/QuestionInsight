from math import *
x = float(input())


if (x <= -1) or (x >= 1):
	f = abs(x) ** (1 / 2)
	print(round(f, 2))
elif (-1 < x) and (x < 0) or (0 < x) and (x < 1):
	f = abs(x)
	print(round(f, 2))
elif (x == 0):
	f = 0
	print(round(f, 2))