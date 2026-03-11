cidade = input()
idade = int(input())

pV= 500
santarem = 370
belem = 600
tefe = 360
tBt = 550

print("Entradas:", cidade, ",", idade)

if(idade>-1 and idade<=2):
	preco = 0
elif(idade>2 and idade <=12):
	if(cidade == "Porto Velho"):
		preco = pV/2
	elif(cidade == "Santarem"):
		preco = santarem/2
	elif(cidade == "Belem"):
		preco = belem/2
	elif(cidade == "Tefe"):
		preco = tefe/2
	elif(cidade == "Tabatinga"):
		preco = tBt/2
elif(idade>12 and idade<=64):
	if(cidade == "Porto Velho"):
		preco = pV
	elif(cidade == "Santarem"):
		preco = santarem
	elif(cidade == "Belem"):
		preco = belem
	elif(cidade == "Tefe"):
		preco = tefe
	elif(cidade == "Tabatinga"):
		preco = tBt
elif(idade>64 and idade <=150):
	if(cidade =="Porto Velho"):
		preco = pV - pV*0.3
	elif(cidade == "Santarem"):
		preco = santarem - santerem*0.3
	elif(cidade == "Belem"):
		preco = belem - belem*0.3
	elif(cidade == "Tefe"):
		preco = tefe - tefe*0.3
	elif(cidade == "Tabatinga"):
		preco = tBt - tBt*0.3

if((idade<0 or idade >150) or (cidade != "Santarem" and cidade != "Belem" and cidade != "Tefe" and cidade !="Tabatinga" and cidade != "Porto Velho")):
	print("entradas invalidas")
if((cidade=="Porto Velho" or cidade== "Santarem" or cidade == "Belem" or cidade =="Tefe" or cidade == "Tabatinga") and (idade>-1 and idade<=150)):
	print("Passagem: R$", round(preco,2))
