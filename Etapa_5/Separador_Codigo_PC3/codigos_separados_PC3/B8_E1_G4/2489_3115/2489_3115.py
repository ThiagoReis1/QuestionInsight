d = input("")
i = int(input(""))
print("Entradas:",d,",",i)
if(d=="Porto Velho")or(d=="Santarem")or(d=="Belem")or(d=="Tefe")or(d=="Tabatinga")and(i>0)and(i<150):
	if(i>0)and(i<=2)or(d=="Porto Velho")or(d=="Santarem")or(d=="Belem")or(d=="Tefe")or(d=="Tabatinga"):
		p = 0
		print("Passagem: R$",round(p,2))
	if(i>=3)and(i<=12)and(d=="Porto Velho"):
		p = 500/2 
		print("Passagem: R$",round(p,2))
	if(i>=3)and(i<=12)and(d=="Santarem"):
		p = 370/2
		print("Passagem: R$",round(p,2))
	if(i>=3)and(i<=12)and(d=="Belem"):
		p = 600/2
		print("Passagem: R$",round(p,2))
	if(i>=3)and(i<=12)and(d=="Tefe"):
		p = 360/2
		print("Passagem: R$",round(p,2))
	if(i>=3)and(i<=12)and(d=="Tabatinga"):
		p = 550/2
		print("Passagem: R$",round(p,2))
	elif(i>=65)and(d=="Porto Velho"): 
		p = (30/100)*500
		print("Passagem: R$",round(p,2))
	elif(i>=65)and(d=="Santarem"):
		p = (30/100)*370
		print("Passagem: R$",round(p,2))	
	elif(i>=65)and(d=="Belem"):
		p = (30/100)*600
		print("Passagem: R$",round(p,2))
	elif(i>=65)and(d=="Tefe"):
		p = (30/100)*360
		print("Passagem: R$",round(p,2))
	elif(i>=65)and(d=="Tabatinga"):
		p = (30/100)*550
		print("Passagem: R$",round(p,2))
	if(i>12)and(i<65)and(d=="Porto Velho"):
		p = 500
		print("Passagem: R$",round(p,2))
	if(i>12)and(i<65)and(d=="Santarem"):
		p = 370
		print("Passagem: R$",round(p,2))
	if(i>12)and(i<65)and(d=="Belem"):
		p = 600
		print("Passagem: R$",round(p,2))
	if(i>12)and(i<65)and(d=="Tefe"):
		p = 360
		print("Passagem: R$",round(p,2))
	if(i>12)and(i<65)and(d=="Tabatinga"):
		p = 550
		print("Passagem: R$",round(p,2))
else:
	print("entradas invalidas")
