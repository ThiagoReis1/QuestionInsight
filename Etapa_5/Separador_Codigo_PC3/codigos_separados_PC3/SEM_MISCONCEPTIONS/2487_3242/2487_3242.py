x = int(input(""))
y = int(input(""))
z = int(input(""))
if((x>0 and x<5) and (y>0 and y<5) and (z>0 and z<5)):
	if(x == 1):
		cx = 180
	elif(x == 2):
		cx = 230
	elif(x == 3):
		cx = 250
	elif(x == 4):
		cx = 350
		
	if(y == 1):
		cy = 75
	elif(y == 2):
		cy = 110
	elif(y == 3):
		cy = 170
	elif( y == 4):
		cy = 200
		
w = cx + cy
	
	print("Entradas:", x,",",y,",",z)
	print("Calorias:", w, "Cal")
else:
	print("Entradas:", x,",",y,",",z)
	print("Dados invalidos")