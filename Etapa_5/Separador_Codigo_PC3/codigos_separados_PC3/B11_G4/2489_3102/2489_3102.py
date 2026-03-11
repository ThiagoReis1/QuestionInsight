c = input("cidade de destino:")
i = int(input("idade do passageiro:"))

if((c !="Porto Velho" and c != "Santarem" and c != "Belem" and c != "Tefe" and c!= "Tabatinga") or (i<0 or i>150)):
	print("Entradas:",c,",",i)
	print("entradas invalidas")
else:
	if(c=="Porto Velho"):
		if(i<=2):
			v=0
		elif(3<=i<=12):
			v=500/2
		elif(i>=65):
			v=500 - (500*0.3)
		else:
			v=500
	elif(c=="Santarem"):
		if(i<=2):
			v=0
		elif(3<=i<=12):
			v=370/2
		elif(i>=65):
			v=370 - (370*0.3)
		else:
			v=370
	elif(c=="Belem"):
		if(i<=2):
			v=0
		elif(3<=i<=12):
			v=600/2
		elif(i>=65):
			v=600 - (600*0.3)
		else:
			v=600
	elif(c=="Tefe"):
		if(i<=2):
			v=0
		elif(3<=i<=12):
			v=360/2
		elif(i>=65):
			v=360 - (360*0.3)
		else:
			v=360
	else:
		if(i<=2):
			v=0
		elif(3<=i<=12):
			v=550/2
		elif(i>=65):
			v=550 - (550*0.3)
		else:
			v=550
	print("Entradas:",c,",",i)
	print("Passagem: R$",round(v,2))

	

