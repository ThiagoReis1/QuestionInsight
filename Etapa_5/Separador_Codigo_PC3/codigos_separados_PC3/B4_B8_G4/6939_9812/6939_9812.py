var = float(input("Valor total da compra: "))
cod = input("Debito (D), PIX (P) ou Cartao (C): ").upper()

if cod == "C":
	n = int(input("1 ou 2 vezes: "))
	
	if n == 1:
		print(round(var,2))
	
	else:
		total = var + (var * 0.09)
		print(round(total,2))
	
elif cod == "D":
	total = var * 0.81
	print(round(total,2))
	
elif cod == "P":
	total = var * 0.81
	print(round(total,2))