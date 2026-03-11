prato = int(input("prato(1,2,3,4): "))
sobremesa = int(input("sobremesa(1,2,3,4): "))
bebida = int(input("bebida(1,2,3,4): "))

if ((prato >= 1) and (prato <= 4) and (sobremesa >=1) and (sobremesa <= 4) and ( bebida>=1) and (bebida <= 4)):
	if(prato == 1):
		p = 180
	elif(prato == 2):
		p = 230
	elif (prato == 3):
		p = 250
	elif (prato == 4):
		p = 350
	if (sobremesa == 1):
		s = 75
	elif (sobremesa == 2):
		s = 110
	elif (sobremesa == 3):
		s = 170
	elif (sobremesa == 4):
		s = 200
	if (bebida == 1):
		b = 20
	elif (bebida == 2):
		b = 70
	elif (bebida == 3):
		b = 100
	elif (bebida == 4):
		b = 65	
	total = p + s + b
	print("Calorias: ", total, "cal")	
else:
	print("Dados invalidos")