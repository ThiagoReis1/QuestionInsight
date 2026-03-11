np = int(input("Digite o numero do prato: "))
ns = int(input("Digite o numero da sobremesa: "))
nb = int(input("Digite o numero da bebidas: "))

if (np >= 1 and np <=4) and (ns >= 1 and ns <= 4) and (nb >= 1 and nb <= 4):
	if (np == 1):
		calorias = 180
	elif(np == 2):
		calorias = 230
	elif(np == 3):
		calorias = 250
	else:
		calorias = 350
	if(ns == 1):
		calorias = calorias + 75
	elif(ns == 2):
		calorias = calorias + 110
	elif(ns == 3):
		calorias = calorias + 170
	else:
		calorias = calorias + 200
	if(nb == 1):
		calorias = calorias + 20
	elif (nb == 2):
		calorias = calorias + 70
	elif(nb == 3):
		calorias = calorias + 100
	else:
		calorias = calorias + 65
	print("Calorias:", calorias, "cal")
	
		
else:
	print("Dados invalidos")