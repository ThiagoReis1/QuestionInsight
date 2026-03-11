AR= int(input("Quantidade de votos de Ambrosio Rutra:"))
DO= int(input("Quantidade de votos de Demelza Olecram:"))

if(AR>DO):
	msg= "Ambrosio Rutra"
	por= 100 * AR/ (AR + DO)
	print(msg)
	print(round(por, 2))
else:
	msg= "Demelza Olecram"
	por= 100 * DO/ (AR + DO)
	print(msg)
	print(round(por, 2))
	
	