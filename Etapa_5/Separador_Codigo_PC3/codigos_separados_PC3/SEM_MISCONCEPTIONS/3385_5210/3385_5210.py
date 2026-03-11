medida = (input(" "))
valor = float(input(" "))

if(medida == "H"):
	Acre = 2.47105 * valor
	print(round(Acre, 2))
else:
	Ha = valor / 2.47105
	print(round(Ha, 2))