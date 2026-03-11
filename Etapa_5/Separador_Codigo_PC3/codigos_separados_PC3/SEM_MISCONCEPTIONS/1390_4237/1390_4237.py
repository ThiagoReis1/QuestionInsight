minutos = int(input("Tempo em minutos:"))

if (100 < minutos):
	tarifa = (minutos*1.40) + 25
	print(round(tarifa,2))
else:
	tarifa = (minutos*1.20)
	print(round(tarifa,2))