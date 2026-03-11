from math import *

x = float(input())

if x >= -4 and x < 0:
	x = sqrt(abs(x))
	print(round(x, 4))
	
elif x >= 0 and x <= 4:
	x = sqrt(x)
	print(round(x, 4))