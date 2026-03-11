option = input('Bolo ou salgado? ')
quantidade = int(input('Quantidade: '))
cafe = int(input('Cafe: '))

if option == 'B':
	valor = (quantidade * 5) + (cafe * 7.5)
if option == 'S':
	valor = (quantidade * 4) + (cafe * 7.5)

print(valor)