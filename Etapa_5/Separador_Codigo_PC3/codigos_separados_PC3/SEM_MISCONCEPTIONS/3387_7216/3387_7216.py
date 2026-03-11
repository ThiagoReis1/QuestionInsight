unidade = input("unidade (M ou K)")
valor = float(input("valor:"))

if unidade.upper() == "M":
	m = valor/2.35215
	print(round(m,2))
else:
	m = 2.35215*valor
	print(round(m,2))
	

			

	