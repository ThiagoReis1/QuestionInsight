cidade = input("nome da cidade: ").lower()
idade = int(input("idade do passageiro: "))

if cidade == "porto velho" or cidade == "santarem" or cidade == "belem" or cidade == "tefe" or cidade == "tabatinga":
	if idade > 0 and idade < 150:
		if idade <= 2:
			valor = 0.0
			print("Passagem: R$", round(valor, 2))		
		elif cidade == "porto velho":
			if 3 <= idade <= 12:
				valor = 500 / 2
				print("Passagem: R$", round(valor, 2))
			elif idade >= 65:
				valor = 500 - (500 * 0.3)
				print("Passagem: R$", round(valor, 2))
			else:
				valor = 500
				print("Passagem: R$", round(valor, 2))
		elif cidade == "santarem":
			if 3 <= idade <= 12:
				valor = 370 / 2
				print("Passagem: R$", round(valor, 2))
			elif idade >= 65:
				valor = 370 - (370 * 0.3)
				print("Passagem: R$", round(valor,2))
			else:
				valor = 370
				print("Passagem: R$", round(valor,2))
		elif cidade == "belem":
			if 3 <= idade <= 12:
				valor = 600 / 2
				print("Passagem: R$", round(valor,2))
			elif idade >= 65:
				valor = 600 - (600* 0.3)
				print("Passagem: R$", round(valor, 2))
			else:
				valor = 600
				print("Passagem: R$", round(valor,2))
		elif cidade == "tefe":
			if 3 <= idade <= 12:
				valor = 360 / 2
				print("Passagem: R$", round(valor,2))
			elif idade >= 65:
				valor = 360 - (360*0.3)
				print("Passagem: R$", round(valor, 2))
			else:
				valor = 360
				print("Passagem: R$", round(valor,2))
		elif cidade == "tabatinga":
			if 3 <= idade <= 12:
				valor = 550/2
				print("Passagem: R$", round(valor,2))
			elif idade >= 65:
				valor = 550 - (550 * 0.3)
				print("Passagem: R$", round(valor,2))
			else:
				valor = 550
				print("Passagem: R$", round(valor,2))
			
	else:
		print("Entradas invalidas")
else:
	print("Entradas invalidas")