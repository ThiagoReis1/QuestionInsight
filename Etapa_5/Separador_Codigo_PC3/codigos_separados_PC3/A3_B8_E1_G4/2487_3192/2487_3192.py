prato = int(input("numero do prato: "))
sobrem = int(input("numero da sobremesa:"))
beb = int(input("numero da bebida: "))

p = [0, 180, 230, 250, 350]
s = [0, 75, 110, 170, 200]
b = [0, 20, 70, 100, 65]

if( np < 1 or np > 4 or ns < 1 or ns > 4 or nb <1 or nb > 4):
	print("Entradas:", np ,",", ns, "," , nb)
	print("Dados invalidos")
	
elif(1<=np<=4 and 1<=ns<=4 and 1<=nb<=4):
	if(np == 1):
		c1 = p[1]
	elif(np == 2):
		c1 = p[2]
	elif(np == 3):
		c1 = p[3]
	elif(np == 4):
		c1 = p[4]

	if(ns == 1):
		c2 = s[1]
	elif(ns == 2):
		c2 = s[2]
	elif(ns == 3): 
		c2 = s[3]
	elif(ns == 4):
		c2 = s[4]

	if(nb == 1):
		c3 = b[1]
	elif(nb == 2):
		c3 = b[2]
	elif(nb == 3):
		c3 = b[3]
	elif(nb == 4):
		c3 = b[4]

	print("Entradas:", np ,",", ns, "," , nb)
	print("Calorias: ", c1+c2+c3, "cal")



	

	