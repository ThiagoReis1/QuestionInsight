VTC = float(input("Valor total da compra: "))
CP = input("Codigo de pagamento: D/P/C ")

if CP == "D" or CP == "P":
	print(round(VTC * 0.87, 2))
else:
	TJ = input("Em quantas vezes? 1/2 ")
	if TJ == "1":
		print(VTC)
	else:
		print(VTC * 1.08)