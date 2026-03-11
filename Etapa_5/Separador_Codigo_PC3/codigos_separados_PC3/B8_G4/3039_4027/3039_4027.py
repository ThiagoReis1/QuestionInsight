from math import *
x = float(input("Valor de x: "))
if(x >= -1 and x <= 1):
	if((x >= -1 and  x < -(1/2)) or (x > (1/2) and x <= 1)):
		f = asin(x)
	elif(x >= -(1/2) and x <= (1/2)):
		f = acos(x)
	f = degrees(f)
	f = round(f, 2)
	print(f)
else:
	print("entrada invalida")