compras = str(input()).upper

cont = 0

while compras:
	if compras == ("C"):
		compras = 10.50
		print(round(compras, 2))
		cont += 1
		compras = str(input()).upper

print(round(compras, 2))