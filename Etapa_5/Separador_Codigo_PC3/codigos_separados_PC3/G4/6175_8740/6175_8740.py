from math import*
x = float(input("insira o valor de x: "))

if (x >= -4) or (x < 0):
	a = abs(x)
	b = a**(1/2)
	print (round(b,4))
elif (x >= 0) or (x<=4):
	c = x**(1/2)
	print (round(c,4))
else:
	print("entrada invalida")