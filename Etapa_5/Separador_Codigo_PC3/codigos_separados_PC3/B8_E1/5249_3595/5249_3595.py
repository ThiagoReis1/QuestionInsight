prato = int(input())
sobremesa = int(input())
bebida = int(input())

if prato <1 or prato >4 or sobremesa<1 or sobremesa>4 or bebida<1 or sobremesa>4:
	print('Dados invalidos')
else:
	if(prato == 1):
		caloria = 180
	elif(prato == 2):
		caloria = 230
	elif(prato == 3):
		caloria = 250
	elif(prato == 4):
		caloria = 350

	if(sobremesa == 1):
		caloria = caloria+75
	elif(sobremesa == 2):
		caloria = caloria+110
	elif(sobremesa == 3):
		caloria = caloria+170
	elif(sobremesa == 4):
		caloria = caloria+200
		
	if(bebida == 1):
		caloria = caloria+20
		print('Calorias: ',caloria, 'cal')
	elif(bebida ==2):
		caloria = caloria+70
		print('Calorias: ',caloria, 'cal')
	elif(bebida == 3):
		caloria = caloria+100
		print('Calorias: ',caloria, 'cal')
	else:
		caloria = caloria+65
		print('Calorias: ',caloria, 'cal')
			
