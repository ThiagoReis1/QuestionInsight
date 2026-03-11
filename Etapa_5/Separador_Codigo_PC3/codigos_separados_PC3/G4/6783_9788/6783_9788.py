ano = int(input('em qual ano vc nasceu?:'))
P = input('pais:').upper()

idd = (2023 - ano)

if P == "B" and idd >= 18:
	print('sim')
	apta = idd - 18
	print(apta)
	
elif P == "B" and idd < 18:
	print('nao')
	apto = 18 - idd
	print(apto)
	
elif P == "E" and idd >= 16:
	print('sim')
	apta = idd - 16
	print(apta)
	
elif P == "E" and idd < 16:
	print('nao')
	apto = 16 - idd
	print(apto)
	
else:
	print('invalido')
	