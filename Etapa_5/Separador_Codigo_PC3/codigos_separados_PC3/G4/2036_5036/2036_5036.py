bola = input("cor da balinha:")
cont = 0
while bola.upper() != "S":
	if bola.upper() == "PRETA":
		cont = cont + 1
		
	bola = input("cor da bola:")

print(cont)