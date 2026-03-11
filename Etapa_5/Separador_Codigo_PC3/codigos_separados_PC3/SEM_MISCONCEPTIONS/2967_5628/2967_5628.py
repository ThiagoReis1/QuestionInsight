altura = float(input('minha altura: '))
altura2 = float(input('Altura do amigo: '))

limite = 1.37

if (altura >= limite) or (altura2 >= limite):
	if altura > altura2:
		print('Sim')
		print(altura)
	else:
		print('Sim')
		print(altura2)
		
else:
	if altura > altura2:
		print('Nao')
		print(altura)
	else:
		print('Nao')
		print(altura2)