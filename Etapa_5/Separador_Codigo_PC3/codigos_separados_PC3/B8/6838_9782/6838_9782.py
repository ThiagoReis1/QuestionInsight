produtos = input("Insira os produtos (D) doces (S) salgados (I) integrais: ").upper()

i = 0 
valor_total = 0

while i < len(produtos):
	if produtos[i] == "D":
		valor_total += 2.25
	elif produtos[i] == "S":
		valor_total += 4.
	elif produtos[i] == "I":
		valor_total += 6.9
	i += 1
print(round(valor_total,2))