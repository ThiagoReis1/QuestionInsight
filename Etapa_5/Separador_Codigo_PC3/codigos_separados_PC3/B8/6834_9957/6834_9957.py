compras = input().upper()
i = 0
preco = 0

while i < len(compras):
	if compras[i] == "C":
		preco += 10.50
	elif compras[i]== "E":
		preco += 8.75
	elif compras[i] == "P":
		preco += 17.90
	i = i + 1

round2 = round(preco, 2)
print(round2)