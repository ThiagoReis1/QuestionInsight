cid = input("Digite o destino: ").lower()
age = int(input("Digite a idade: "))

if((cid!="porto velho" and cid!="santarem" and cid!="belem" and cid!="tefe" and cid!="tabatinga")):
	print("Entradas invalidas")

if(cid=="porto velho"):
	if(age<0 or age>150):
		print("Entradas invalidas")
	elif(age>0 and age<=2):
		print("Passagem: R$0.00")
	elif(age>=3 and age<=12):
		z = 500/2
		print("Passagem: R$",round(z,2))
	elif(age<=13 and age<=64):
		print("Passagem: R$ 500.0")
	elif(age>=65 or age<150):
		z = 500-(500*0.30)
		print("Passagem: R$",round(z,2))
	else:
		print("Passagem: R$500.0")

if(cid=="santarem"):
	if(age<0 or age>150):
		print("Entradas invalidas")
	if(age>0 and age<=2):
		print("Passagem: R$0.00")
	elif(age>=3 and age<=12):
		z = 370/2
		print("Passagem: R$",round(z,2))
	elif(age<=13 and age<=64):
		print("Passagem: R$370.0")
	elif(age>=65 or age<150):
		z = 370-(370*0.30)
		print("Passagem: R$",round(z,2))
	else:
		print("Passagem: R$370.0")
		
if(cid=="belem"):
	if(age<0 or age>150):
		print("Entradas invalidas")
	if(age>0 and age<=2):
		print("Passagem: R$0.00")
	elif(age>=3 and age<=12):
		z = 600/2
		print("Passagem: R$",round(z,2))
	elif(age>=13 and age<=64):
		print("Passagem: R$600.0")
	elif(age>=65 or age<150):
		z = 600-(600*0.30)
		print("Passagem: R$",round(z,2))
	else:
		print("Passagem: R$600.0")
		
if(cid=="tefe"):
	if(age<0 or age>150):
		print("Entradas invalidas")
	if(age>0 and age<=2):
		print("Passagem: R$0.00")
	elif(age>=3 and age<=12):
		z = 360/2
		print("Passagem: R$",round(z,2))
	elif(age>=13 and age<=64):
		print("Passagem: R$360.0")
	elif(age>=65 or age<150):
		z = 360-(360*0.30)
		print("Passagem: R$",round(z,2))
	else:
		print("Passagem: R$360.0")
		
if(cid=="tabatinga"):
	if(age<0 or age>150):
		print("Entradas invalidas")
	if(age>0 and age<=2):
		print("Passagem: R$0.00")
	elif(age>=3 and age<=12):
		z = 550/2
		print("Passagem: R$",round(z,2))
	elif(age>=13 and age<=64):
		print("Passagem: R$550.0")
	elif(age>=65 or age<150):
		z = 550-(550*0.30)
		print("Passagem: R$",round(z,2))
	else:
		print("Passagem: R$550.0")