from math import*
x = float(input("x: "))
if x <= 4 and x >= -4:
	if x >= -4 and x < 0:
		print(round(abs(x**(1/2)), 4))
	elif x >= 0 and x <= 4:
		print(round(x**(1/2), 4))
else:
	print("entrada invalida")
	