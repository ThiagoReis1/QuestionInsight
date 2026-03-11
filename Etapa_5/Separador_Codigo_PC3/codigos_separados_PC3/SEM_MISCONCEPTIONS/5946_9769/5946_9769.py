merenda = input('L ou P: ')
quantidade = int(input(''))
refri = int(input(''))

if merenda =='L':
	preco_final = (quantidade*6) + (refri * 3)
	
else:
	preco_final= (quantidade*4.5)+(refri*3)


print(preco_final)