## valor = energia * tarifa + taxa de iluminacao publica # de 0 a 350. Apartir de 350, pára.

tarifa = 0
taxa = 0
energia = float(input("entre com um valor para energia: "))

if (energia >= 0 and energia <= 150):
	tarifa = tarifa + 0.60
	taxa = taxa + 5
	valor = energia * tarifa + taxa 
	print(round(valor, 2))
elif (energia > 150 and energia <= 250):
	tarifa = tarifa + 0.65
	taxa = taxa + 8
	valor = energia * tarifa + taxa
	print(round(valor, 2))
elif (energia > 250 and energia <= 350):
	tarifa = tarifa + 0.70
	taxa = taxa + 12
	valor = energia * tarifa + taxa
	print(round(valor, 2))
else:	
	tarifa = tarifa + 0.75
	taxa = taxa + 16
	valor = energia * tarifa + taxa
	print(round(valor, 2))
	
	