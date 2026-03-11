consumo = float(input("Consumo em minutos: "))
if consumo <= 100:
	tarifa= (consumo * 1.20)
	print(round(tarifa,2))
else:
	tarifa= (consumo * 1.40) + 25
	print(round(tarifa,2))