from math import *
x = float(input("Digite um numero: "))
if x <= 0 :
	y = 0
	print(round(y, 4))
elif 0 < x <= 1 :
	y = 1
	print(round(y, 4))
elif 1 < x <= 2 :
	y = abs(x**(1/2))
	print(round(y, 4))
else:
	y = abs(x**(1/3))
	print(round(y, 4))