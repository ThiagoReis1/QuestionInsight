destino = input("cidade de destino: ").lower()

idade = int(input("idade do passageiro: "))

if (idade > 0 and idade < 150):
	if(destino == "porto velho" and idade <= 2):
		passagem = 500
		print("Passagem: R$ ", passagem)
	elif(destino == "porto velho" and idade < 3 and idade <= 12):
		passagem = 500
		z = passagem / 2
		print("Passagem: R$ ", z)	
	elif(destino == "porto velho" and idade >= 65):
		passagem = 500
		desc = passagem * 0.3
		z = passagem - desc
		print("Passagem: R$ ", z)	
	elif (destino == "santarem" and idade <= 2):
		passagem = 370
		print("Passagem: R$ ", passagem)
	elif (destino == "santarem" and idade > 3 and idade <= 12):
		passagem = 370
		z = passagem / 2
		print("Passagem: R$ ", z)	
	elif (destino == "santarem" and idade >= 65):
		passagem = 370
		desc = passagem * 0.3
		z = passagem - desc
		print("Passagem: R$ ", z)
	elif (destino == "belem" and idade <= 2):
		passagem = 600
		print("Passagem: R$ ", passagem)	
	elif (destino == "belem" and idade > 3 and idade <= 12):
		passagem = 600
		z = passagem / 2
		print("Passagem: R$ ", z)
	elif (destino == "belem" and idade >= 65):
		passagem = 600
		desc = passagem * 0.3
		z = passagem - desc
		print("Passagem: R$ ", z)
	elif (destino == "tefe" and idade <= 2):
		passagem = 360
		print("Passagem: R$ ", passagem)	
	elif (destino == "tefe" and idade > 3 and idade <= 12):
		passagem = 360
		z = passagem / 2
		print("Passagem: R$ ", z)	
	elif (destino == "tefe" and idade >= 65):
		passagem = 360
		desc = passagem * 0.3
		z = passagem - desc
		print("Passagem: R$ ", z)
	elif (destino == "tabatinga" and idade <= 2):
		passagem = 550
		print("Passagem: R$ ", passagem)
	elif (destino == "tabatinga" and idade > 3 and idade <= 12):
		passagem = 550
		z = passagem / 2
		print("Passagem: R$ ", z)
	elif (destino == "tabatinga" and idade >= 65):
		passagem = 550
		desc = passagem *0.3
		z = passagem - desc
		print("Passagem: R$ ", z)
else:
	print("Entradas invalidas")