item = input('Digite o item: ')
quant = int(input('Digite a quantidade de itens: '))
quantrelf = int(input('Digite a quantidade de relfs: '))

if item.upper() == 'P':
	total = quant * 4.50 + quantrelf * 3.00
else:
	total = quant * 6.00 + quantrelf * 3.00

print(round(total, 2))
