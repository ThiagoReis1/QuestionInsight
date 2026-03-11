x = float(input("digite o numero de x: "))
if x >= -100 and x < 0:
	z = -1 * (1 / x)
	print(round(z, 4))
elif x > 0 and x <= 100:
	z = 1 / x
	print(round(z, 4))
else:
	print("entrada invalida")
