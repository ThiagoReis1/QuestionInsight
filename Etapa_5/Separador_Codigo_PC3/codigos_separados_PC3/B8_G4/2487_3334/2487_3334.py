x = int(input("X : "))
y = int(input("Y : "))
z = int(input("Z : "))

if(( x > 4 ) or (x < 1) and ( y > 4 ) or (y < 1) and ( z > 4 ) or (z < 1)):
	print ("Entradas:", x ,"," , y ,"," , z)
	print ("Dados invalidos")
else:
	if( x == 1):
		xx = 180

	elif ( x == 2):
		xx = 230

	elif ( x == 3):
		xx = 250

	elif ( x == 4):
		xx = 350

	if( y == 1):
		yy = 75

	elif ( y == 2):
		yy = 110

	elif ( y == 3):
		yy = 170

	elif ( y == 4):
		yy = 200

	if( z == 1):
		zz = 20

	elif ( z == 2):
		zz = 70

	elif ( z == 3):
		zz = 100

	elif ( z == 4):
		zz = 65

	w = xx + yy + zz 

	print ("Entradas:", x ,"," , y ,"," , z)
	print ("Calorias:", w , "cal")