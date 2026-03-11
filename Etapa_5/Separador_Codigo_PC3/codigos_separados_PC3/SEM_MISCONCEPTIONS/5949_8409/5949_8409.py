bolo_ou_croissant = input("B/C:")
quant_comidas = int(input("quantidades_c:"))
quantidade_bebidas = int(input("quantidade_b:"))

if bolo_ou_croissant == "B":
	preco_total = (quant_comidas * 3) + (quantidade_bebidas * 5.50)
else:
	preco_total = (quant_comidas * 6) + (quantidade_bebidas * 5.50)


print(round(preco_total,2))

