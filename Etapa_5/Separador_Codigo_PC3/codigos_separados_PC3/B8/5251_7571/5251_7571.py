destino=input("digite o destino: ").upper()
idade=int(input("digite a idade: "))

if(destino=="PORTO VELHO" and idade<=2):
	print("Passagem: R$ 500.00")
if(destino=="PORTO VELHO" and idade>=3 and idade<=12):
	total=500/2
	print("Passagem: R$",total)
if(destino=="PORTO VELHO" and idade>=65):
	desconto=500*30/100
	total=500-desconto
	print("Passagem: R$",total)
elif(destino=="SANTAREM" and idade<=2):
	print("Passagem: R$",370.00)
if(destino=="SANTAREM" and idade>=3 and idade<=12):
	total=370/2
	print("Passagem: R$",total)
if(destino=="SANTAREM" and idade>=65):
	desconto=370*30/100
	total=370-desconto
	print("Passagem: R$",total)
elif(destino=="BELEM" and idade<=2):
	print("Passagem: R$ 600")
if(destino=="BELEM" and idade>=3 and idade<=12):
	total=600/2
	print("Passagem: R$", total)
if(destino=="BELEM" and idade>=65):
	desconto=600*30/100
	total=600-desconto
	print("Passagem: R$",total)
if(destino=="TEFE" and idade<=2):
	print("Passagem: R$ 360")
if(destino=="TEFE" and idade>=3 and idade<=12):
	total= 360/2
	print("Passagem: R$", total)
if(destino=="TEFE" and idade>=65):
	desconto=360*30/100
	total=360-desconto
	print("Passagem: R$",total)
elif(destino=="TABATINGA" and idade<=2):
	print("Passagem: R$ 550")
if(destino=="TABATINGA" and idade>=3 and idade<=12):
	total=550/2
	print("Passagem: R$",total)
if(destino=="TABATINGA" and idade>=65):
	desconto=550*30/100
	total=550-desconto
	print("Passagem: R$",total)
else:
	print("entradas invalidas")
		
