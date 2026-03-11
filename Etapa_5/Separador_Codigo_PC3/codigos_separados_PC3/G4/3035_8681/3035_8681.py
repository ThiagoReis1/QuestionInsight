from math import *

a = float(input("Insira o valor em graus: "))
x = radians(a)

if (0 <= a <=360):
	if ((0 <= a < 90) or (180<= a < 270)):
		y = sin(x)
		print(round(y,4))
	elif ((90 <= a < 180) or (270 <= a <360)):
		y = cos(x)
		print(round(y,4))
	else:
		print("entrada invalida")
else:
	print("entrada invalida")

	
