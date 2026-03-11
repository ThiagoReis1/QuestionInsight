a = input("cidade de destino: ")
b = float(input("idade do passageiro: "))
if (a == "porto velho"):
	if (b<=2):
		print ("Nao paga")
	elif (b>=3) and (b<=12):
		c = 500/2
		print("Passagem: R$",(round(c,2)))
	elif (b>=65):
		c = 
		print("Passagem; R$",(round(c,2)))
	else:
		print("Passagem: R$500.00")
elif (a == "santarem"):
	if (b<=2):
		print ("Nao paga")
	elif (b>=3) and (b<=12):
		c = 370/2
		print("Passagem: R$",(round(c,2)))
	elif (b>=65):
		c = 370*30/100
		print("Passagem: R$",(round(c,2)))
	else:
		print ("Passagem: R$370.00")
elif (a == "belem"):
	if (b<=2):
		print ("Nao paga")
	elif (b>=3) and (b<=12):
		c = 600/2
		print("Passagem: R$",(round(c,2)))
	elif (b>=65):
		c = 600*30/100
		print("Passagem: R$",(round(c,2)))
	else:
		print ("Passagem: R$600.00")
elif (a == "tefe"):
	if (b<=2):
		print ("Nao paga")
	elif (b>=3) and (b<=12):
		c = 360/2
		print("Passagem: R$",(round(c,2)))
	elif (b>=65):
		c = 360*30/100
		print("Passagem: R$",(round(c,2)))
	else:
		print ("Passagem: R$360.00")
elif (a == "tabatinga"):
	if (b<=2):
		print ("Nao paga")
	elif (b>=3) and (b<=12):
		c = 550/2
		print("Passagem: R$",(round(c,2)))
	elif (b>=65):
		c = 550*30/100
		print("Passagem: R$",(round(c,2)))
else:
	print("Entrada invalida")
		