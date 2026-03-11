from math import * 

x = float(input("Entrada:"))

if x >= -4 and x < 0:
	x = x * -1
	print(round(abs(x) ** (1/2),4))
elif x == 0:
	print(round(0,4))
elif x > 0 and x <= 4:
	print(round(abs(x) ** (1/2), 4))
else:
	print("Entrada Invalida")