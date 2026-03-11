compra = float(input("Valor da compra: "))
way = input("Forma de pagamento: ").upper()
if way == 'D' or way == 'P':
	total = (compra - (compra * 0.12))
	print(round(total , 2))
if way == 'C':
	parc = int(input("parcelas: "))
	if parc == 1:
		print(round(compra, 2))
	elif parc == 2:
		total = (compra + (compra * 0.07))
		print(round(total , 2))