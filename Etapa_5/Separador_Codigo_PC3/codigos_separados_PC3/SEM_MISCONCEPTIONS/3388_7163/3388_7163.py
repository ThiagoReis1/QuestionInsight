unidade = str(input("btu ou watt :"))
medida = float(input("qual a medida:"))

medida1 = 3.41214 * medida
medida2 = medida / 3.41214

if (unidade .upper() == "W"):
	print(round(medida1,2))
else:
	print(round(medida2,2))