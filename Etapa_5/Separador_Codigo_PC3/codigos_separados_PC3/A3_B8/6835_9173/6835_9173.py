produtos = input("insira os itens de compra -(B) biscoitos (C) cereais (E) enlatados: ").upper()
total = 0
i = 0
cont_b = 0
cont_c = 0
cont_e = 0
while i < len(produtos):
	if produtos[i] == "B":
		total += 3.75
		cont_b += 1
	elif produtos[i] == "C":
		total += 7.90
		cont_c += 1
	elif produtos[i] == "E":
		total += 9.85
		cont_e += 1
	i += 1
print(round(total, 2))
