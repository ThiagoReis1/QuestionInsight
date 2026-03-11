from math import *
x = float(input("insira um valor de x: "))

if (x <= -1) or (x >= 1):
	f = x ** 2
	print(round(f, 4))
elif (x > -1) and (x < 0) or (x > 0) and (x < 1):
	f = x
	print(round(f, 4))
elif (x == 0):
	f = 1
	print(round(f, 4))