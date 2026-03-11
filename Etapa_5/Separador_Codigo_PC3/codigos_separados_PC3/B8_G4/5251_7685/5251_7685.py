c= input("cidade destino: ").upper()
i= int(input("idade: "))

if(0<i<=150)and((c=="PORTO VELHO")or(c=="SANTAREM")or(c=="BELEM")or(c=="TEFE")or(c=="TABATINGA")):
	if(i<=2):
		k=0.0
		print("Passagem: R$", round(k, 2))
	elif(c=="PORTO VELHO")and(12>=i>=3):
		k=500/2
		print("Passagem: R$", round(k, 2))
	elif(c=="PORTO VELHO")and(i>=65):
		k=500-500*30/100
		print("Passagem: R$", round(k, 2))
	elif(c=="PORTO VELHO")and(12<i<65):
		k=500
		print("Passagem: R$", round(k, 2))
	elif(c=="SANTAREM")and(12>=i>=3):
		k=370/2
		print("Passagem: R$", round(k, 2))
	elif(c=="SANTAREM")and(i>=65):
		k=370-370*30/100
		print("Passagem: R$", round(k, 2))
	elif(c=="SANTAREM")and(12<i<65):
		k=370
		print("Passagem: R$", round(k, 2))
	elif(c=="BELEM")and(12>=i>=3):
		k=600/2
		print("Passagem: R$", round(k, 2))
	elif(c=="BELEM")and(i>=65):
		k=600-600*30/100
		print("Passagem: R$", round(k, 2))
	elif(c=="BELEM")and(12<i<65):
		k=600
		print("Passagem: R$", round(k, 2))
	elif(c=="TEFE")and(12>=i>=3):
		k=360/2
		print("Passagem: R$", round(k, 2))
	elif(c=="TEFE")and(i>=65):
		k=360-360*30/100
		print("Passagem: R$", round(k, 2))
	elif(c=="TEFE")and(12<i<65):
		k=360
		print("Passagem: R$", round(k, 2))
	elif(c=="TABATINGA")and(12>=i>=3):
		k=550/2
		print("Passagem: R$", round(k, 2))
	elif(c=="TABATINGA")and(i>=65):
		k=550-550*30/100
		print("Passagem: R$", round(k, 2))
	elif(c=="TABATINGA")and(12<i<65):
		k=550
		print("Passagem: R$", round(k, 2))
else:
	print("Entradas invalidas")