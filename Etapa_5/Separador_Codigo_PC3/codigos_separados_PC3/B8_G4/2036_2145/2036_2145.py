bola = input("Resultado: ").upper()
c = 0

while (bola != "S"):
	if(bola == "PRETA"):
		c = c + 1
		bola = input("Resultado: ").upper()
	elif(bola == "VERMELHA"):
		bola = input("Resultado: ").upper()
print (c)