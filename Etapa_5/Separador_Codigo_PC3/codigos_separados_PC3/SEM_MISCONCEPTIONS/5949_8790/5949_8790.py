item = input("'B' para bolo e 'C' para croissant: ")
qtde = int(input("qtde de fatias: "))
qtde_bebida = int(input("quantidade de cappuccino: "))

if  item == 'B':
	total = (3*qtde) + (5.50 * qtde_bebida)
	print(round(total,2))
else:
	total = (6*qtde) + (5.50*qtde_bebida)
	print(round(total))
	
	