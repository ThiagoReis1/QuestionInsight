import math
x = float(input())

if (x >= -4 and x < 0):
	fx = abs(x) ** (1/2)
	print(round(fx, 4))
elif (x >= 0 and x <= 4):
	fx = x ** (1/2)
	print(round(fx, 4))
else:
	print("entrada invalida")

