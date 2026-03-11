x = input("Cidade de destino: ")
y = int(input("idade do passageiro: "))

print("Entradas: ", x, ",", y)

if (((x != "Porto Velho") and (x != "Santarem") and (x != "Belem") and (x != "Tefe") and (x != "Tabatinga")) or ((y < 0) or (y > 150))):
	print("entradas invalidas")
elif (y <= 2):
	z = 0
	print("Passagem: R$", round(z,2))
elif ((x == "Porto Velho") and ((y >= 3) and (y <= 12))):
	z = 250.00 
	print("Passagem: R$", round(z,2))
elif ((x == "Santarem") and ((y >= 3) and (y <= 12))):
	z = 135.00
	print("Passagem: R$", round(z,2))
elif ((x == "Belem") and ((y >= 3) and (y <= 12))):
	z = 300.00
	print("Passagem: R$", round(z,2))
elif ((x == "Tefe") and ((y >= 3) and (y <= 12))):
	z = 180.00
	print("Passagem: R$", round(z,2))
elif ((x == "Tabatinga") and ((y >= 3) and (y <= 12))):
	z = 275.00
	print("Passagem: R$", round(z,2))
elif (x == "Porto Velho") and (y >= 65):
	m = 500.00 * (30/100)
	z = 500.00 - m
	print ("Passagem: R$", round(z,2))
elif (x == "Santarem") and (y >= 65):
	m = 370.00 * (30/100)
	z = 370.00 - m
	print ("Passagem: R$", round(z,2))
elif (x == "Belem") and (y >= 65):
	m = 600.00 * 30/100
	z = 600.00 - m
	print ("Passagem: R$", round(z,2))
elif (x == "Tefe") and (y >=65):
	m = 360.00 * 30/100
	z = 360.00 - m
	print ("Passagem: R$", round(z,2))
elif (x == "Tabatinga") and (y >= 65):
	m = 550.00 * 30/100
	z = 550.00 - m
	print ("Passagem: R$", round(z,2))
	
