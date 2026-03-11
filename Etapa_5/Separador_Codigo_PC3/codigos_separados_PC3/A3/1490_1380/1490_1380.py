volume = float(input("Informe o volume de comsumo em metros cubicos: "))
tarifa = 0.00
taxa = 0.00

if (volume <= 10.0):
	tarifa = 3.00
	taxa = 15.00
elif (volume <= 15.0):
	tarifa = 3.50
	taxa = 20.00
elif (volume <= 20.0):
	tarifa = 4.00
	taxa = 25.00
else:
	tarifa = 4.50
	taxa = 30.00

valor = volume * tarifa + taxa

print(round(valor,2))