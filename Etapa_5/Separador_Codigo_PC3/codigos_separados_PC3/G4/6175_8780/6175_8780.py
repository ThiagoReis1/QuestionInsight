x = float(input("Digite o valor de x: "))

from math import *

if x < -4 or x > 4:
	print("entrada invalida")
else:
	if x >= -4 and x < 0:
		y = sqrt(abs(x))
	else:
		y = sqrt(x)
		
print(round(y, 4))