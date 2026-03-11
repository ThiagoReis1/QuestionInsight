consumo = float(input("Digite consumo: "))

if (consumo >= 0) and (consumo <= 10):
	tarifa = 3
	taxa = 15
	valor = consumo * tarifa + taxa
	print(round(valor, 2))
elif (consumo > 10) and (consumo <= 15):
	tarifa = 3.5
	taxa = 20
	valor = consumo * tarifa + taxa
	print(round(valor, 2))
elif (consumo > 15) and (consumo <= 20):
	tarifa = 4
	taxa = 25
	valor = consumo * tarifa + taxa
	print(round(valor, 2))
elif (consumo > 20):
	tarifa = 4.5
	taxa = 30
	valor = consumo * tarifa + taxa
	print(round(valor, 2))