pr = int(input("numero do prato: "))
sobre = int(input("numero de sobremesa: "))
be = int(input("numero de bebida: "))

if(pr >= 1  and pr <= 4 ) and (sobre >= 1 and sobre  <= 4) and (be >=1 and be <= 4):
	if(pr == 1):
		b = 180
		
	elif(pr == 2):
		b = 230
		
	elif( pr == 3):
		b = 250
		
	elif( pr == 4):
		b = 350
		
	if(sobre == 1):
		c = 75
		
	elif(sobre == 2):
		c = 110
		
	elif(sobre == 3 ):
		c = 170
		
	elif(sobre == 4):
		c = 200
		
	if(be == 1):
		d = 20
		
	elif(be == 2):
		d = 70
		
	elif(be == 3):
		d = 100
		
	elif(be == 4):
		d = 65
		
		
	print("Calorias:" ,b +c+d,"cal")
else:
	print("Dados invalidos")
	
	