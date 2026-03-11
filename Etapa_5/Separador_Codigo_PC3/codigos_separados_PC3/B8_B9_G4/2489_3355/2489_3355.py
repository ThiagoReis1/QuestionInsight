a = input("Cidade de destino: ")
b = int(input("Idade do passageiro: "))

print("Entradas:",a,",",b)
if (((a == "Porto Velho") or (a == "Santarem") or (a == "Belem") or (a == "Tefe") or (a == "Tabatinga")) and ((b>=0) and (b <= 150))):
	if ((b > 2) and (b <= 12)):
		if (a == "Porto Velho"):
			p = 500/2
			print("Passagem: R$",round(p, 2))
		elif (a == "Santarem"):
			p = 370/2
			print("Passagem: R$",round(p, 2))
		elif (a == "Belem"):
			p = 600/2
			print("Passagem: R$",round(p, 2))
		elif (a == "Tefe"):
			p = 360/2
			print("Passagem: R$",round(p, 2))
		elif (a == "Tabatinga"):
			p = 550/2
			print("Passagem: R$",round(p, 2))
	elif (b >= 65):
		if (a == "Porto Velho"):
			p = 500*0.7
			print("Passagem: R$",round(p, 2))
		elif (a == "Santarem"):
			p = 370*0.7
			print("Passagem: R$",round(p, 2))
		elif (a == "Belem"):
			p = 600*0.7
			print("Passagem: R$",round(p, 2))
		elif (a == "Tefe"):
			p = 360*0.7
			print("Passagem: R$",round(p, 2))
		elif (a == "Tabatinga"):
			p = 550*0.7
			print("Passagem: R$",round(p, 2))
	elif ((b>12) and (b<65)):
		if (a == "Porto Velho"):
			p = 500
			print("Passagem: R$",round(p, 2))
		elif (a == "Santarem"):
			p = 370
			print("Passagem: R$",round(p, 2))
		elif (a == "Belem"):
			p = 600
			print("Passagem: R$",round(p, 2))
		elif (a == "Tefe"):
			p = 360
			print("Passagem: R$",round(p, 2))
		elif (a == "Tabatinga"):
			p = 550
			print("Passagem: R$",round(p, 2))
	else:
		print("Passagem: R$ 0,00")
else:
	print("entradas invalidas")