ataque = input('Ataque: ').upper()
baforada = int(input('Quantidade: '))
if ataque == 'MARITIMO':
	uni_destruida = baforada * 40
	print('Viserion')
	print(uni_destruida)
if ataque == 'TERRESTRE':
	uni_destruida = baforada * 150
	print('Drogon')
	print(uni_destruida)