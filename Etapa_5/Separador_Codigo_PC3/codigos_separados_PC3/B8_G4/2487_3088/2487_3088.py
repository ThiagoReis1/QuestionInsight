np = int(input("Insira o numero do prato: "))
ns = int(input("Insira o numero da sobremesa: "))
nb = int(input("Insira o numero da bebida: "))
if (1<=np<=4):
	if np==1:
		x= 180
	elif np==2:
		x = 230
	elif np==3:
		x = 250
	elif np==4: 
		x = 350
		
if (1<=ns<=4):
	if ns==1:
		y = 75
	elif ns==2:
		y = 110
	elif ns==3:
		y = 170
	elif ns==4: 
		y = 200

if (1<=nb<=4):
	if nb==1:
		z = 20
	elif nb==2:
		z = 70
	elif nb==3:
		z = 100
	elif nb==4: 
		z = 65
if not ((1<=np<=4) and (1<=ns<=4) and (1<=nb<=4)):
	print("Entradas:",np,",",ns,",",nb)
	print("Dados invalidos")
else:
	print("Entradas:",np,",",ns,",",nb)
	print("Calorias:",x+y+z,"cal")

		