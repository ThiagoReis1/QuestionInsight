d=input("Cidade de destino: ")
i=int(input("Idade: "))

if d.upper()=="PORTO VELHO" or d.upper()=="SANTAREM" or d.upper()=="BELEM" or d.upper()=="TEFE" or d.upper()=="TABATINGA":
	if 0<=i and i<=2:
		p=0
		print("Passagem: R$", round(p,2))
	elif d.upper()=="PORTO VELHO":
		if 3<=i and i<=12:
			p=500/2
			print("Passagem: R$", round(p,2))
		elif 12<i and i<65:
			p=500
			print("Passagem: R$",round(p,2))
		elif 65<=i and i<=150:
			p=500-(500*0.3)
			print("Passagem: R$", round(p,2))
		else:
			print("Entradas invalidas")
	elif d.upper()=="SANTAREM":
		if 3<=i and i<=12:
			p=370/2
			print("Passagem: R$", round(p,2))
		elif 12<i and i<65:
			p=370
			print("Passagem: R$", round(p,2))
		elif 65<=1 and i<=150:
			p=370-(370*0.3)
			print("Passagem: R$", round(p,2))
		else:
			print("Entradas invalidas")
	elif d.upper()=="BELEM":
		if 3<=i and i<=12:
			p=600/2
			print("Passagem: R$", round(p,2))
		elif 12<i and i<65:
			p=600
			print("Passagem: R$", round(p,2))
		elif 65<=i and i<=150:
			p=600-(600*0.3)
		else:
			print("Entradas invalidas")
	elif d.upper()=="TEFE":
		if 3<=i and i<=12:
			p=360/2
			print("Passagem: R$", round(p,2))
		elif 12<i and i<65:
			p=360
			print("Passagem: R$", round(p,2))
		elif 65<=i and i<=150:
			print("Passagem: R$", round(p,2))
		else:
			print("Entradas invalidas")
	elif d.upper()=="TABATINGA":
		if 3<=i and i<=12:
			p=550/2
			print("Passagem: R$", round(p,2))
		elif 12<i and i<65:
			p=550
			print("Passagem: R$", round(p,2))
		elif 65<=i and i<=150:
			p=550-(550*0.3)
			print("Passagem: R$", round(p,2))
		else:
			print("Entradas invalidas")
else:
	print("Entradas invalidas")
		