itens = input('coloque os tipos de produtos que voce comprou: ').upper()

i = 0 # indice
total = 0 # total da compra (acumulador)

while i < len(itens):
	if itens[i] == 'H':
		total += 5.40
	elif itens[i] == 'C':
		total += 8.95
	elif itens[i] == 'L':
		total += 4.50
	i +=1
print(round(total, 2))