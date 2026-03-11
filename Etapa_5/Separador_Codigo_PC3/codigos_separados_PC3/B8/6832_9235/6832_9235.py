compra = input("digite a sequencia: ")
preco_t = 0

for i in range(len(compra)):
	if compra[i] == "H":
		preco_t += 5.40
	elif compra[i] == "C":
		preco_t += 8.95
	elif compra[i] == "L":
		preco_t += 4.50

preco_t = round(preco_t, 2)
print(preco_t)