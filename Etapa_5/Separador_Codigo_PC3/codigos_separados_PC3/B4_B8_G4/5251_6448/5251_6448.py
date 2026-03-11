d= input("Cidade de destino: ").lower()
i= int(input("Idade do passageiro: "))

#if (d!="porto velho") or (d!="santarem") or (d!="belem") or (d!="tefe") or (d!="tabatinga"):
#	print("Entradas invalidas")

if (i>=0) and (i<=2):
	p=0
	print("Passagem: R$",p)
elif (i>=3) and (i<=12):
	if (d=="porto velho"):
		p = (500)*(0.50)
		print("Passagem: R$",round(p,2))
	elif (d=="santarem"):
		p=370*0.50
		print("Passagem: R$",round(p,2))
	elif (d=="belem"):
		p=600*0.50
		print("Passagem: R$",round(p,2))
	elif (d=="tefe"):
		p=360/2
		print("Passagem: R$",rounf(p,2))
	elif(d=="tabatinga"):
		p=550/2
		print("Passagem: R$:",round(p,2))
elif (i>=65) and (i<150):
	if (d=="porto velho"):
		p=500*0.70
		print("Passagem: R$",round(p,2))
	elif(d=="santarem"):
		p=370*0.70
		print("Passagem: R$",round(p,2))
	elif (d=="belem"):
		p=600*0.70
		print("Passagem: R$",round(p,2))
	elif (d=="tefe"):
		p=360*0.70
		print("Passagem: R$",round(p,2))
	elif (d=="tabatinga"):
		p=550*0.70
		print("Passagem: R$",round(p,2))
elif (i>150):
	print("Entradas invalidas")
elif (i<0):
	print("Entradas invalidas")
"""elif (d!="porto velho"):
	print("Entradas invalidas")
elif (d!="santarem"):
	print("Entradas invalidas")
elif (d!="belem"):
	print("Entradas invalidas")
elif (d!="tefe"):
	print("Entradas invalidas")
elif (d!="tabatinga"):
	print("Entradas invalidas")"""