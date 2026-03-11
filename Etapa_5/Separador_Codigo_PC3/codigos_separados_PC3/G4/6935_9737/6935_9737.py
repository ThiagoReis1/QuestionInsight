tt = float(input("Total da compra: "))
opc = input("Forma de Pagamento: ").upper()

if opc == "C":
	par = int(input("1 ou 2: "))
	if par == 2:
		tt2 = tt + tt * (7/100)
		print(round(tt2,2))
	else:
		print(round(tt,2))
elif opc == "D":
	d = tt - tt * (12/100)
	print(round(d,2))
else:
	p = tt - tt * (12/100)
	print(round(p,2))