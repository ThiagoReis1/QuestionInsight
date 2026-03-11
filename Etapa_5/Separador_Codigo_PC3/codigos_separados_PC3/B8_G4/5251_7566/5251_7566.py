x = input("insira a cidade de destino: ")
y = int(input("insira a idade: "))
if(x == "porto velho") or (x == "tefe") or (x == "santarem") or (x == "belem") or (x == "tabatinga"):
	if(0<y<=150):
		if(y<=2):
			z = 0.0
		elif(3<=y<=12):
			if (x == "belem"):
				z = 600/2
			elif(x == "porto velho"):
				z = 500/2
			elif(x == "santarem"):
				z = 370/2
			elif(x == "tefe"):
				z = 360/2
			elif(x == "tabatinga"):
				z = 550/2
		elif(65<=y<=150):
			if(x == "belem"):
				z = 600 - 600*0.3
			elif(x == "porto velho"):
				z = 500 - 500*0.3
			elif(x == "santarem"):
				z = 370 - 370*0.3
			elif(x == "tefe"):
				z = 360 - 360*0.3
			elif(x == "tabatinga"):
				z = 550 - 550*0.3
		elif(12<y<65):
			if(x == "porto velho"):
				z = 500.0
			elif(x == "santarem"):
				z = 370.0
			elif(x == "belem"):
				z = 600.0
			elif(x ==  "tefe"):
				z = 360.0
			elif(x == "tabatinga"):
				z = 550.0
		print("Passagem: R$", round(z, 2))
	else:
		print("Entradas invalidas")
else:
	print("Entradas invalidas")
	
