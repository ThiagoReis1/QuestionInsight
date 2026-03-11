from math import *
x = float(input())
if (0<=x and x<90) or (180<=x and x<270):
	x = radians(x)
	print(round(sin(x),4))
elif (90<=x and x<180) or (270<=x and x<360):
	x = radians(x)
	print(round(cos(x),4))
else:
	print("entrada invalida")