consumo = float(input("Consumo: "))
minuto = 100/60
tarifa = consumo + 1.20*minuto
taxa = consumo + 25.00 + 1.40*minuto
if (consumo > 100):
	print (tarifa+taxa)
else:
	print (tarifa)
