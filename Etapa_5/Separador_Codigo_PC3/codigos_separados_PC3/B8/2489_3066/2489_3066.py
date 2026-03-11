destino = input("Digite: ")
idade = int(input("Digite: "))


if ((destino != "Porto Velho") and (destino != "Santarem") and (destino != "Belem") and (destino != "Tefe" ) and (destino != "Tabatinga") or (idade < 0) or (idade > 150)):
	print("Entradas invalidas")
else:
	if (idade <= 2):
		print("Passagem: R$", 0)
	else: 
		if (idade >= 3) and (idade <= 12):
			if (destino == "Porto Velho"):
				valor = 500
				valor_total = valor / 2
				print(valor_total)
			elif (destino == "Santarem"):
				valor = 370
				valor_total = valor / 2
				print("Passagem: R$", valor_total)
			elif (destino == "Belem"):
				valor = 600
				valor_total = valor / 2
				print(valor_total)
			elif (destino == "Tefe"):
				valor = 360
				valor_total = valor / 2
				print("Passagem: R$", valor_total)
			elif (destino == "Tabatinga"):
				valor = 550
				valor_total = valor / 2
				print("Passagem: R$", valor_total)
		else:
			if (idade >= 65):
				if (destino == "Porto Velho"):
					valor = 500
					d = valor * 30 / 100
					vt = valor - d
					print("Passagem: R$", vt)
				elif (destino == "Santarem"):
					valor = 370
					d = valor * 30 / 100
					print("Passagem: R$", vt)
				elif (destino == "Belem"):
					valor = 600
					d = valor * 30 / 100
					vt = valor - d
					print("Passagem: R$", vt)
				elif (destino == "Tefe"):
					valor = 360
					d = valor * 30 / 100
					vt = valor - d
					print("Passagem: R$", vt)
				elif (destino == "Tabatinga"):
					valor = 550
					d = valor * 30 / 100
					vt = valor - d
					print("Passagem: R$", vt)
