produtos = input('itens: ').upper()

i = 0
total = 0 #total das compras

while i < len(produtos):
	if produtos[i] == 'D':
		total += 2.25
	elif produtos[i] == 'S':
		total += 4.
	elif produtos[i] == 'I':
		total += 6.9
	i += 1
print(round(total, 2))