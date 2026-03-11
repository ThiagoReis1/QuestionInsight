pacote= int(input("insira seu número:"))


if pacote < 50:
	total= 60.00 + 4.50
	print(round(total,2))
elif pacote == 50:
	total= 60.00 + 5.50
	print(round(total, 2))
elif pacote > 50:
	total= 60.00 + 6.50
	print(round(total, 2))