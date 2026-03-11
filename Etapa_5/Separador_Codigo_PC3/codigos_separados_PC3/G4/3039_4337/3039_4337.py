from math import *
x = float(input())

if(-1 <= x < -0.5 or 0.5 < x <=1):
	print(round(degrees(asin(x)),2))
elif(-0.5 <= x <= 0.5):
	print(round(degrees(acos(x)),2))
else:
	print("entrada invalida")