valorcompra = float(input("valor total da compra:"))
forma = input("D, P ou C").upper()

if forma == "D":
	total = valorcompra - (valorcompra * 0.19)
	print(round(total, 2))
elif forma == "P":
	total = valorcompra - (valorcompra * 0.19)
	print(round(total, 2))
elif forma == "C":
	parcelas = int(input("numero de parcelas:"))
	if parcelas == 1:
		total = valorcompra
		print(round(total, 2))
	elif parcelas == 2:
		total = valorcompra + (valorcompra * 0.09)
		print(round(total, 2))