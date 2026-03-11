d=input("Insira destino: ")
idade= int(input("idade: "))
print("Entradas: ",d,",",idade)
if(idade>0 and idade<150 and (d=="Porto_Velho" or d=="Santarem" or d=="Belem" or d=="Tefe" or d=="Tabatinga")):
	if(d=="Porto_Velho" and idade<=2):
		p=round(0)
		print("Passagem: ","R$",p)
	elif(d=="Porto_Velho" and 3<=idade<=12):
		p=round(500/2,2)
		print("Passagem: ","R$",p)
	elif(d=="Porto_Velho" and idade>=65):
		p=round(500-(500*30/100), 2)
		print("Passagem: ","R$",p)
	elif(d=="Santarem" and idade<=2):
		p=round(0)
		print("Passagem: ","R$",p)
	elif(d=="Santarem" and 3<=idade<=12):
		p=round(370/2,2)
		print("Passagem: ","R$", p)
	elif(d=="Santarem" and idade>=65):
		p=round(370-(370*30/100),2)
		print("Passagem: ","R$",p)
	elif(d=="Belem" and idade<=2):
		p=round(0)
		print("Passagem: ","R$",p)
	elif(d=="Belem" and 3<=idade<=12):
		p=round(600/2,2)
		print("Passagem: ","R$", p)
	elif(d=="Belem" and idade>=65):
		p=round(600-(600*30/100),2)
		print("Passagem: ","R$",p)
	elif(d=="Tefe" and idade<=2):
		p=round(0)
		print("Passagem: ","R$", p)
	elif(d=="Tefe" and 3<=idade<=12):
		p=round(360/2,2)
		print("Passagem: ","R$", p)
	elif(d=="Tefe" and idade>=65):
		p=round(360-(360*30/100),2)
		print("Passagem: ","R$",p)
	elif(d=="Tabatinga" and idade<=2):
		p=round(0)
		print("Passagem: ","R$",p)
	elif(d=="Tabatinga" and 3<=idade<=12):
		p=round(550/2,2)
		print("Passagem: ","R$",p)
	elif(d=="Tabatinga" and idade>=65):
		p=round(550-(550*30/100),2)
		print("Passagem: ","R$",p)
	else:
		print("entradas invalidas")
else:
	print("entradas invalidas")
		
		
		