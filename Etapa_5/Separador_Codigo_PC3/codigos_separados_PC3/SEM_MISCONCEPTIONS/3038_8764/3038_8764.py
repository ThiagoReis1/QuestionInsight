#from math import *
x = float(input("Digite o valor de x: "))

if (x <= -1) or (x >= 1):
	valor = abs(x)**(1/2)
	print(round(valor, 2))
elif (x > -1) and (x < 0) or (x > 0) and (x < 1):
	valor = abs(x)
	print(round(valor, 2))
else:
	valor = 0
	print(round(valor, 2))