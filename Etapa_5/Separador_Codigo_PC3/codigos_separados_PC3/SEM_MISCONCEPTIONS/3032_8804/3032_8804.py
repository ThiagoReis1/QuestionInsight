from math import *

x = float(input("Valor de x: "))

if x <= 0:
	total = 0
	print(round(total,4))
elif 0 < x and x <=1:
	total = 1
	print(round(total,4))
elif 1 < x and x <=2:
	total = sqrt(x)
	print(round(total,4))
else:
	total = x**(1/3)
	print(round(total,4))
