np = int(input("numero do prato: "))
ns = int(input("numero da sobremesa: "))
nb = int(input("numero da bebida: "))

if (1<=np<=4) or (1<=ns<=4) or (1<=nb<=4):
	if(np == 1):
		prato = 180
	elif(np == 2):
		prato = 230
	elif(np == 3):
		prato = 250
	elif(np == 4):
		prato = 350
	
	if(ns == 1):
		sobremesa = 75
	elif(ns == 2):
		sobremesa = 110
	elif(ns == 3):
		sobremesa = 170
	elif (ns == 4):
		sobremesa = 200
	
	if(nb == 1):
		bebida = 20
	elif(nb == 2):
		bebida = 70
	elif(nb == 3):
		bebida = 100
	elif(nb == 4):
		bebida = 65
	
	valor = prato + sobremesa + bebida
	print("Calorias:",valor,"cal")
	
else:
	print("Dados invalidos")