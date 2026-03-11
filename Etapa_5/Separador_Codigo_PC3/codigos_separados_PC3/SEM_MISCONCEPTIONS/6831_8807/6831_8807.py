
produtos = input("Produtos: ").upper()

i = 0
cont = 0

while i < len(produtos):
	if produtos[i] == "A":
		cont += 16.75
	elif produtos[i] == "L":
		cont += 4.60
	else:
		produtos[i] == "P"
		cont += 2.85
	i += 1
	total = cont
print(round(total, 2))