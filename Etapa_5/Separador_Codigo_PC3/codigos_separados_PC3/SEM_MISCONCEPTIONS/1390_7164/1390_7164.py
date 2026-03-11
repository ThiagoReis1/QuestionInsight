consumo = float(input("Consumo em minutos: "))
if (consumo <= 100):
	print(round(1.2*consumo,2))
else:
	print(round(25 + 1.4*consumo,2))