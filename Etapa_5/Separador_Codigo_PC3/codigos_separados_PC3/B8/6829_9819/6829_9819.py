itens = input("coloque os tipos de produtos que vc comprou: ").upper()

i = 0 
total = 0

while i < len(itens):
	if itens[i] == 'A':
		total += 19.9
	elif itens[i] == "L":
		total += 3.5
	elif itens[i] == "P":
		total += 4.25
	i += 1

print(round(total, 2))