tempo = float(input("digite o tempo: "))

if tempo < 2:
	tarifa = 5.00 + 1.25
	print(round(tarifa, 2))
elif tempo == 2:
	tarifa = 5.00 + 2.25
	print(round(tarifa, 2))
elif tempo > 2:
	tarifa = 5.00 + 3.25
	print(round(tarifa, 2))
	