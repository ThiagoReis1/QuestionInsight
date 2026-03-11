face= input("cara ou coroa:").upper()
jogadas_cara= 0

while face != "S":
	if face == "CARA":
		jogadas_cara= jogadas_cara + 1
	face= input("cara ou coroa:").upper()
print(jogadas_cara)
		

