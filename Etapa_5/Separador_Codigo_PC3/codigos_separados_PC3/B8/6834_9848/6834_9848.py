itens = input('coloque os tipos de produtos que vc comprou')

i = 0 # indice
total = 0 # total das compras(acumulador)

while i < len(itens):
	if itens[i] =='C':
		total += 10.50
	elif itens[i] == 'E':
		total += 8.75
	elif itens[i] =='P':
		total += 17.90
	i += 1 
print(round(total, 2))