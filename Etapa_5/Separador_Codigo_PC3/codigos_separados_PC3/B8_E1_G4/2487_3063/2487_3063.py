x = int(input("digite o numero: "))	
y = int(input("digite o numero: "))
z = int(input("digite o numero: "))

print("Entradas: ",x,", ",y,", ",z)

# Dados Invalidos

if(x < 1 or x > 4 or y < 1 or y > 4 or z < 1 or z > 4):
	print("Dados invalidos")
else: 
	
	#Coluna X

	if(x == 1):
		c = 180
	elif(x == 2):
		c = 230
	elif(x == 3):
		c = 250
	elif(x == 4):
		c = 350

	# Coluna Y

	if(y == 1):
		w = 75
	elif(y == 2):
		w = 110
	elif(y == 3):
		w = 170
	elif(y == 4):
		w = 200

	#Coluna Z

	if(z == 1):
		j = 20
	elif(z == 2):
		j = 70
	elif(z == 3):
		j = 100
	elif(z == 4):
		j = 65

	print("Calorias: ",(c + w + j),"cal")	


	
	
