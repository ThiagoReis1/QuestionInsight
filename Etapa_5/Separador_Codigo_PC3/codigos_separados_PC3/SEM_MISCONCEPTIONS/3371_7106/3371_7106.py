medida = input("Medida:  ")
valor = float(input("Valor:  "))
if medida == "K":
	conv = (valor/1.60934)
	print(round(conv, 2))
else:
	conv = (valor*1.60934)
	print(round(conv, 2))
