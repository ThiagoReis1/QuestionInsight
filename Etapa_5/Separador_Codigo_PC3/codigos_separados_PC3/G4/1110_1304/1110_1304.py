x = int(input("Insira um prato: "))
y = int(input("Insira uma sobremesa: "))
z = int(input("Insira uma bebida: "))
if ( (x > 0 and x <5) and (y >0 and y <5) and (z >0 and z <5)):
	if ( x == 1 or x == 2 or x ==3 or x== 4):
		if ( x == 1):
			c1 = 180
		elif ( x == 2):
			c1 = 230
		elif ( x == 3):
			c1 = 250
		else:
			c1 = 350
	if ( y == 1 or y == 2 or y ==3 or y ==4):
		if ( y == 1):
			c2 = 75
		elif ( y == 2):
			c2 = 110
		elif ( y == 3):
			c2 = 170
		else:
			c2 = 200
	if ( z == 1 or z ==2 or z ==3 or z ==4):
		if( z
			== 1 ):
			c3 = 20
		elif ( z == 2):
			c3 = 70
		elif ( z == 3):
			c3 = 100
		else:
			c3 = 65
	C = c1 +c2 +c3
	print("Entradas:",x, ",", y, ",", z)
	print("Calorias:", C, "cal")
else:
	print("Entradas:",x, ",", y, ",", z)
	print("Dados invalidos")