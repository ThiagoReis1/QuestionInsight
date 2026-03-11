item = input('Digite seu item (L/P):')
quant = int(input('Digite a quantidade:'))
refri = int(input('Digite a quantidade de refrigerantes:'))

lanche = 6
pizza = 4.5
bebida = 3 * refri

if(item.upper() == 'L'):
	total = lanche * quant + bebida
	print(round(total, 2))

if(item.upper() == 'P'):
	total = pizza * quant + bebida
	print(round(total, 2))
