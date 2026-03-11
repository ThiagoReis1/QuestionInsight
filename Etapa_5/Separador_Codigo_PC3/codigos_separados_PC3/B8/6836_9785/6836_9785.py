itens = input('coloque os tipos de produtos que vc comprou: ').upper()

i = 0
total = 0

while i < len(itens):
	if itens[i] == 'B':
		total += 6.80
	elif itens[i] == 'C':
		total += 11.75
	elif itens[i] == 'M':
		total += 5.90	
	i += 1
print(round(total, 2))