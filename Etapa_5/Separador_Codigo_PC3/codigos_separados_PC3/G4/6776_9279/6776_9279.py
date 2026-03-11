nasc = int(input('data que nasceu'))
pais = input('pais')
idade = 2023 - nasc

if pais.upper() == 'B':
	if idade >= 18:
		print('sim')
		val = idade - 18
		print(val)
	
	else:
		print('nao')
		val = 18 - idade
		print(val)
		
elif pais.upper() == 'R':
	if idade >= 17:
		print('sim')
		val = idade - 17
		print(val)
		
	else:
		print('nao')
		val = 17 - idade
		print(val)
		
else:
	print('invalido')