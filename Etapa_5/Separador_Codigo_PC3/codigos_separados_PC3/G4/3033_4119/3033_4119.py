x = float(input("digite um falor de x: "))
if ((-100 <= x) and (x < 0)):
	y = -1/x
else:
	if ((0 < x) and (x <= 100)):
		y = 1/x
	else:
			y = str("entrada invalida")
print (round(y,4))