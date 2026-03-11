x = float(input())

from math import *

if((-1 <= x) and (x < -1/2) or (1/2 < x) and (x <= 1)):
	a = degrees(asin(x))
	print(round(a, 2))
elif((-1/2 <= x) and (x <= 1/2)):
	a = degrees(acos(x))
	print(round(a, 2))
else:
	print("entrada invalida")