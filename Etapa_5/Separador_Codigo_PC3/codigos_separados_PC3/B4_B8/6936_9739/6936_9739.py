valor_da_compra = float(input("Informe o valor da compra: "))
cod = input("Informe o codigo: ").upper()

if cod == "D":
	total = valor_da_compra - valor_da_compra * (13/100)
	print(round(total, 2))
elif cod == "P":
	total = valor_da_compra - valor_da_compra * (13/100)
	print(round(total, 2))

elif cod == "C":
	par = input("Informe se voce quantas parcelas vc quer: ")
	if par == 1:
		total = valor_da_compra
		print(round(total, 2))
	else:
		total = valor_da_compra + valor_da_compra * (8/100)
		print(round(total, 2))