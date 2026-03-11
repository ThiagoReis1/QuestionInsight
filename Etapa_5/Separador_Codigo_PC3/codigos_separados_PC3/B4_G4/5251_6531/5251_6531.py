c = input("Cidade de destino: ")
d = int(input("Idade do passageiro: "))

print("Entradas:",c,",",d)

if(d > 0   and d < 150):
	if((c == "Porto Velho") and (d <= 2)):
		print("Passagem: R$ ", 0.0)
	elif(c == "Porto Velho" and 3 <= d <= 12):
		print("Passagem: R$",round(500 / 2, 2))
	elif(c == "Porto Velho" and d >= 65):
		print("Passagem: R$",round( 500-(500 * 0.30), 2))
	elif(c == "Santarem" and d <= 2):
		print("Passagem: R$ 0.0")
	elif(c == "Santarem" and 3 <= d <= 12):
		print("Passagem: R$",round(370 / 2, 2))
	elif(c == "Santarem" and d >= 65):
		print("Passagem: R$",round(370-(370 * 0.30), 2))
	elif(c == "Belem" and d <= 2):
		print("Passagem: R$ 0.0")
	elif(c == "Belem" and 3 <= d <= 12):
		print("Passagem: R$",round(600/2, 2))
	elif(c == "Belem" and d >= 65):
		print("Passagem: R$",round(600-(600*0.30), 2))
	elif(c == "Tefe" and d <= 2):
		print("Passagem: R$ 0.0")
	elif(c == "Tefe" and 3 <= d <= 12):
		print("Passagem: R$",round(360/2, 2))
	elif(c == "Tefe" and d >= 65):
		print("Passagem: R$",round(360-(360*0.30), 2))
	elif(c == "Tabatinga" and d <= 2):
		print("Passagem: R$ 0.0")
	elif(c == "Tabatinga" and 3 <= d <= 12):
		print("Passagem: R$",round(550/2, 2))
	elif(c == "Tabatinga" and d >= 65):
		print("Passagem: R$",round(550-(550*0.30), 2))
	else:
		print("entradas invalidas")
else:
	print("entradas invalidas")
