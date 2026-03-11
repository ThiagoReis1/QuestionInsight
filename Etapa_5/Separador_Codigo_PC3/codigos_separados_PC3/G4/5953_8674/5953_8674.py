item = (input('indique o item: '))
qtde = float(input('quntidade de itens: '))
refri = float(input('quantidade de refri: '))

if item == 'L':
	a = qtde * 6 + refri * 3
	print(round(a , 2))
else:
	a = qtde * 13.50 + refri * 3
	print(round(a , 2))