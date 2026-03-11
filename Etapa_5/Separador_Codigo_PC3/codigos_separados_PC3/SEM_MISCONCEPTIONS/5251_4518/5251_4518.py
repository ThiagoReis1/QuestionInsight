cidade = input()
idade = int(input())

if (idade >= 0 and idade <= 2) and (cidade == "Porto Velho" or cidade == "Santarem" or cidade == "Belem" or cidade == "Tefe" or cidade == "Tabatinga"):
	preco = 0.0
	print("Entradas:", cidade, ",", idade)
	print("Passagem: R$", preco)
	
elif cidade == "Porto Velho":
	if idade >= 3 and idade <= 12:
		preco = 500.0 - (500 * 0.5)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade >= 65 and idade <= 150:
		preco = 500.0 - (500 * 0.3)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade > 12 and idade < 65:
		preco = 500.0
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	else:
		print("Entradas:", cidade, ",", idade)
		print("entradas invalidas")
		
elif cidade == "Santarem":
	if idade >= 3 and idade <= 12:
		preco = 370.0 - (370 * 0.5)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade >= 65 and idade <= 150:
		preco = 370.0 - (370 * 0.3)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade > 12 and idade < 65 :
		preco = 370.0
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	else:
		print("Entradas:", cidade, ",", idade)
		print("entradas invalidas")
		
elif cidade == "Belem":
	if idade >= 3 and idade <= 12:
		preco = 600.0 - (600 * 0.5)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade >= 65 and idade <= 150:
		preco = 600.0 - (600 * 0.3)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade > 12 and idade < 65:
		preco = 600.0
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	else:
		print("Entradas:", cidade, ",", idade)
		print("entradas invalidas")
		
elif cidade == "Tefe":
	if idade >= 3 and idade <= 12:
		preco = 360.0 - (360 * 0.5)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade >= 65 and idade <= 150:
		preco = 360.0 - (360 * 0.3)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade > 12 and idade < 65:
		preco = 360.0
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	else:
		print("Entradas:", cidade, ",", idade)
		print("entradas invalidas")
		
elif cidade == "Tabatinga":
	if idade >= 3 and idade <= 12:
		preco = 550.0 - (550 * 0.5)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade >= 65 and idade <= 150:
		preco = 550.0 - (550 * 0.3)
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	elif idade > 12 and idade < 65:
		preco = 550.0
		print("Entradas:", cidade, ",", idade)
		print("Passagem: R$", preco)
		
	else:
		print("Entradas:", cidade, ",", idade)
		print("entradas invalidas")
		
	
else: 
	print("Entradas:", cidade, ",", idade)
	print("entradas invalidas")
