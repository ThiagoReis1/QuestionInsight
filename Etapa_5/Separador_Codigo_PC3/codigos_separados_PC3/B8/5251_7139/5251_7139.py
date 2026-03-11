# Entrada 

destino = (input("Destino:"))
idade = int(input("Idade:"))

print("Entradas:", destino, ",", idade)

#Condicao 1

if destino.upper() == "PORTO VELHO":
	valor = 500
elif destino.upper() == "SANTAREM":
	valor = 370
elif destino.upper() == "BELEM":
	valor = 600
elif destino.upper() == "TEFE":
	valor = 360
elif destino.upper() == "TABATINGA":
	valor = 550
else:
	print("entradas invalidas")
	
# Condicao 2

if (idade > 0) and (idade < 150):
	if (idade <= 2):
		total = (valor * 0)
		print("Passagem: R$ ",total)
	elif (idade >= 3) and (idade <= 12):
		total = round(valor / 2,2)
		print("Passagem: R$ ",total)
	elif (idade >= 65):
		total = round(valor - (valor * 30/100),2)
		print("Passagem: R$ ",total)
else:
	print("entradas invalidas")
		
		