idade = int(input(''))
peso = float(input(''))
print('Entradas:', idade,'anos e', peso, 'kg')
if 0 <= idade <= 130 and 0 < peso<= 550:
	if idade >= 12:
		if peso >= 60:
			dosagem = 1000
			print('Dosagem:', dosagem, 'mg')
		elif peso < 60:
			dosagem = 875
			print('Dosagem:', dosagem, 'mg')
	elif idade < 12:
		if peso <= 5:
			dosagem = 75
			print('Dosagem:', dosagem, 'mg')
		elif 5 < peso <= 9:
			dosagem = 125
			print('Dosagem:', dosagem, 'mg')
		elif 9 <peso<= 16:
			dosagem = 250
			print('Dosagem:', dosagem, 'mg')
		elif 16 < peso <= 24:
			dosagem = 375
			print('Dosagem:', dosagem, 'mg')
		elif 24 <peso<= 30:
			dosagem = 500
			print('Dosagem:', dosagem, 'mg')
		elif peso > 30:
			dosagem = 750
			print('Dosagem:', dosagem, 'mg')
else:
	print('Dados invalidos')
	