regiao = input('nome da regiao:')
if(regiao == 'Ponta Tempestade' or regiao == 'Ilha do Dragao' or regiao == 'Campina' or regiao == 'Winterfell' or regiao == 'Rochedo Casterly' or regiao == 'Pyke' or regiao == 'Correrio' or regiao == 'Ninho da Aguia' or regiao == 'Dorne'):
	if(regiao == 'Ponta Tempestade'):
		print('Baratheon')
	elif(regiao == 'Ilha do dragao'):
		print('Targaryen')
	elif(regiao == 'Campina'):
		print('Tyrell')
	elif(regiao == 'Winterfell'):
		print('Stark')
	elif(regiao == 'Rochedo Casterly'):
		print('Lannister')
	elif(regiao == 'Pyke'):
		print('Greyjoy')
	elif(regiao == 'Correrio'):
		print('Tully')
	elif(regiao == 'Ninho da Aguia'):
		print('Arryn')
	elif(regiao == 'Dorne'):
		print('Martell')
else:
	print('Entrada', regiao, 'invalida')