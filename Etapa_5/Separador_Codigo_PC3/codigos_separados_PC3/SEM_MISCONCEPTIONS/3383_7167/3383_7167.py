medida = input("Unidade de medida (L/K)")

if (medida == "K"):
	valor = float(input("K: "))
	conversao = 2.20462 * valor
	print(round(conversao, 2))
else:
	valor = float(input("lb: "))
	conversao = valor/2.20462
	print(round(conversao, 2))
	