consumo = float(input("Consumo de minutos: "))

if(consumo <= 100):
	tarifa = 1.2 * consumo 
	print(round(tarifa, 2))

else:
	taxa = 25
	tarifa = (1.40 * consumo) + taxa
	print(round(tarifa, 2))
	