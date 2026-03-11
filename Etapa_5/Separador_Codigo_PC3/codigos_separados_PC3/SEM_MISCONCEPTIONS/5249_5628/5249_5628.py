prato = int(input('numero do prato: '))
sobre = int(input('Numero da Sobremesa: '))
bebida = int(input('Numero da bebida: '))


if (prato >= 1 and prato <= 4) and (sobre >= 1 and sobre <= 4) and (bebida >= 1 and bebida <= 4):
	if prato == 1:
		calP = 180
	elif prato == 2:
		calP = 230
	elif prato == 3:
		calP = 250
	else:
		calP = 350

	if sobre == 1:
		calS = 75
	elif sobre == 2:
		calS = 110
	elif sobre == 3:
		calS = 170
	else:
		calS = 200

	if bebida == 1:
		calB = 20
	elif bebida == 2:
		calB = 70
	elif bebida == 3:
		calB = 100
	else:
		calB = 65
	total = (calP + calS + calB)
	print('Calorias:',total, 'cal')
else:
	print('Dados invalidos')

