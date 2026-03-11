from math import*
x = float(input ("escreva o valor de x: "))

if (x >= -1 and x < -1/2) or (x > 1/2 and x <= 1) :
	z = asin(x)
	print(round(z, 2))
elif x >= -1/2 and x <= 1/2:
	z = acos(x)
	print(round(z, 2))
else: 
	print("entrada invalida")
	
