a = input("genero: ").upper()
b = input("subgenero: ").upper()
if(a == "INVESTIGATIVA" or a == "DRAMATICA") and (b == "SUSPENSE" or b == "DRAMA" or b == "COM FICCAO" or b == "AVENTURA"):
	if(a == "INVESTIGATIVA" and b == "SUSPENSE"):
		print("DEXTER")
	elif(a == "INVESTIGATIVA" and b == "DRAMA"):
		print("NARCOS")
	elif(a == "DRAMATICA" and b == "COM FICCAO"):
		print("LOST")
	elif(a == "DRAMATICA" and b == "AVENTURA"):
		print("SHERLOCK")
else:
	print("SERIE NAO IDENTIFICADA")
