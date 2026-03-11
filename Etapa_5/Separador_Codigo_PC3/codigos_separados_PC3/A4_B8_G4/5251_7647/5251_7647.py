cd = input("Insira a Cidade de Destino: ")
id = int(input("Insira a Idade do Passageiro: "))

if(cd == "porto velho"):
	if(id<=2 and id>0):
		pp = 0
		print("Passagem: R$", round(pp,2))
	elif(id>=3 and id<=12):
		pp = 500.00 / 2
		print("Passagem: R$", round(pp,2))
	elif(id>=65):
		pp = 500.00 - (500.00 * 0.3)
		print("Passagem: R$", round(pp,2))
		
elif(cd == "santarem"):
	if(id<=2 and id>0):
		pp = 0
		print("Passagem: R$", round(pp,2))
	elif(id>=3 and id<=12):
		pp = 370.00 / 2
		print("Passagem: R$", round(pp,2))
	elif(id>=65 and id<150):
		pp = 370.00 - (370.00 * 0.3)
		print("Passagem: R$", round(pp,2))
	else:
		print("Entradas invalidas")

elif(cd == "belem"):
	if(id<=2 and id>0):
		pp = 0
		print("Passagem: R$", round(pp,2))
	elif(id>=3 and id<=12):
		pp = 600.00 / 2
		print("Passagem: R$", round(pp,2))
	elif(id>=65):
		pp = 600.00 - (600.00 * 0.3)
		print("Passagem: R$", round(pp,2))
		
elif(cd == "tefe"):
	if(id<=2 and id>0):
		pp = 0
		print("Passagem: R$", round(pp,2))
	elif(id>=3 and id<=12):
		pp = 360.00 / 2
		print("Passagem: R$", round(pp,2))
	elif(id>=65):
		pp = 360.00 - (360.00 * 0.3)
		print("Passagem: R$", round(pp,2))

elif(cd == "tabatinga"):
	if(id<=2 and id>0):
		pp = 0
		print("Passagem: R$", round(pp,2))
	elif(id>=3 and id<=12):
		pp = 550.00 / 2
		print("Passagem: R$", round(pp,2))
	elif(id>=65 and id<150):
		pp = 550.00 - (550.00 * 0.3)
		print("Passagem: R$", round(pp,2))
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")