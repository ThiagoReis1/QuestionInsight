nasc = int(input('Digite seu ano de nascimento:'))
pais = input('Digite sua nacionalidade:')

idade = 2023 - nasc

if pais.upper() == 'B':
	if idade >= 18:
		print('sim')
		print(idade - 18)
	else:
		print('nao')
		print(18 - idade)
		
elif pais.upper() == 'R':
	if idade >= 17:
		print('sim')
		print(idade - 17)
	else:
		print('nao')
		print(17 - idade)

else:
	print('invalido')
		
		
		
	
	