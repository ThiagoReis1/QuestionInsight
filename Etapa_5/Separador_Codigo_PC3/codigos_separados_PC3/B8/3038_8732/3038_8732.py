from math import *

x = float(input("Valor de x: "))
if (x <= -1) or (x >= 1):
	valor = abs(x) ** (1/2)
	print(round(valor, 2))
else:
	if ( -1 < x < 0) or (0 < x < 1):
		valor = abs(x)
		print(round(valor, 2))
	else:
		if ( x == 0):
			valor = 0
			print(round(valor, 2))