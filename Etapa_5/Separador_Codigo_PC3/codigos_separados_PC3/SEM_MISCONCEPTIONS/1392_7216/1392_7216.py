consumo = float(input("coloque o consumo de agua (em m3): "))
if consumo < 10: 
	tarifa = 3*consumo+30
	print(tarifa)
else:	
	tarifa = 3.50*consumo+30
	print(round(tarifa,2))