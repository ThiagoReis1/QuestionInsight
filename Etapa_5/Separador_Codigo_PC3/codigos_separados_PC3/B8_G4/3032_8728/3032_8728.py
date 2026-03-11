from math import*
x = float(input("valor: "))

if (x <= 0):
	print(round(0,4))
elif (0 < x <= 1):
	print(round(1,4))
elif (1 < x <= 2):
	print(round(x**(1/2),4))
elif (x>2):
	print(round(x**(1/3),4))