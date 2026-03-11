bola = input("PRETA ou VERMELHA: ").upper()

n = 0
while(bola != "S"):
	print(bola)
	if(bola == "PRETA"):
		bola = input("PRETA ou VERMELHA: ").upper()
		n = n+1
	elif(bola == "VERMELHA"):
		bola = input("PRETA ou VERMELHA: ").upper()
	elif(bola == "S"):
		print(n)
	
