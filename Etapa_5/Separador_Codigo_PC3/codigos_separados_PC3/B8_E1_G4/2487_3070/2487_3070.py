x = int(input("numero do prato: "))
y = int(input("numero da sobremesa: "))
z = int(input("numero da bebida: "))

if((x < 1) or (x > 4) or (y < 1) or (y > 4) or (z < 1) or (z > 4)):
	print("Entradas:", x, ",", y, ",", z)
	print("Dados invalidos")
else:
	if(x == 1):
		c1 = 180
	elif(x == 2):
		c1 = 230
	elif(x == 3):
		c1 = 250
	elif(x == 4):
		c1 = 350

	if(y == 1):
		c2 = 75
	elif(y == 2):
		c2 = 110
	elif(y == 3):
		c2 = 170
	elif(y == 4):
		c2 = 200

	if(z == 1):
		c3 = 20
	elif(z == 2):
		c3 = 70
	elif(z == 3):
		c3 = 100
	elif(z == 4):
		c3 = 65
	
	w = c1 + c2 + c3

	print("Entradas:", x, ",", y, ",", z)
	print("Calorias:", w, "cal")