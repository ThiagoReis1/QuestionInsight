nome= input("grito ou toque: ")
nome=(nome.lower())
D1= int(input("D1: "))
D2= int(input("D2: "))

if(nome== "grito"):
	danos=(D1+D2+6)
	print(danos)
	
else:
	danos= (D1+D2)**2
	print(danos)
