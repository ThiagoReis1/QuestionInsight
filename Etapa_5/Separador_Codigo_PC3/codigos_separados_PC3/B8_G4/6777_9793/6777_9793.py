an = int(input('an: '))
pais = input('B/I: ')
pais = pais.upper()

age = 2023 - an

if pais == 'B':
	if age >= 18:
		print('sim')
		print(age - 18)
	else:
		print('nao')
		print(18 - age)
elif pais == 'I':
	if age >= 17:
		print('sim')
		print(age - 17)
	else:
		print('nao')
		print(17 - age)
