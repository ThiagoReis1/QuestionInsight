c = input("cidade: ")
i = int(input("idade: "))


#if (c != "porto velho" or "santarem" or "belem" or "tefe" or "tabatinga") or (i < 0) and (i > 150):
#	print("Entradas invalidas")
#elif (c == "porto velho"):
if (i > 0) and (i <= 150) and (c == "porto velho" or "tefe" or "belem" or "santarem" or "tabatinga"): 
	if (c == "porto velho"):
		x = 500.00
	elif (c == "santarem"):
		x = 370.00
	elif (c == "belem"):
		x = 600.00
	elif (c == "tefe"):
		x = 360.00
	elif (c == "tabatinga"):
		x = 550.00
	else:
		print("Entradas invalidas")
		
	if (i <= 2):
		passagem = 0.0
	elif (i >= 3) and (i <= 12):      #*
		passagem = x/2
	elif (i >= 65):
		passagem = x*0.7
	else:
		passagem = x
		print("Passagem: R$", round(passagem, 2))


