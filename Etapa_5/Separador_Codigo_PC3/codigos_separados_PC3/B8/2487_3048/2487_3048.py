x = int(input("o numero do prato: "))
y = int(input("o numero da sobremesa: "))
z = int(input("o numero da bebida: "))

print("Entradas:", x, ",", y, ",", z)

if((x <= 4) or (y <= 4) or (z <= 4)):
	if(x == 1):
		calorias = 180
	elif(x == 2):
		calorias = 230
	elif(x == 3):
		calorias = 250
	elif(x == 4):
		calorias = 350
	if(y == 1):
		calorias1 = 75
	elif(y == 2):
		calorias1 = 110
	elif(y == 3):
		calorias1 = 170
	elif(y == 4):
		calorias1 = 200
	if(z == 1):
		calorias2 = 20
	elif(z == 2):
		calorias2 = 70
	elif(z == 3):
		calorias2 = 100
	elif(z == 4):
		calorias2 = 65
	
	W = calorias + calorias1 + calorias2
	print("Calorias: ", W, " cal")
else:
	print("Dados invalidos")

	



			 
