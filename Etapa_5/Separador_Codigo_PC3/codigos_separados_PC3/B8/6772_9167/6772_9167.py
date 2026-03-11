valor = float(input("custa a compra: "))
pag = input("metodo de pagamento: ").lower()

if pag == "d" or pag == "p":
	x = valor-valor*0.17
	print(round(x, 2))
else:
	if pag == "c2":
		total = valor+valor*0.08
		print(round(total, 2))
	else:
		if pag == "c1":
			a = valor
			print(round(a, 2))
