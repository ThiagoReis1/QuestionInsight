consumo=float(input("consumo de minutos:"))
if	(consumo>100):
	tarifa=25+(1.40*consumo)
	print(round(tarifa,2))
else:
	tarifa=1.20*consumo
	print(round(tarifa,2))