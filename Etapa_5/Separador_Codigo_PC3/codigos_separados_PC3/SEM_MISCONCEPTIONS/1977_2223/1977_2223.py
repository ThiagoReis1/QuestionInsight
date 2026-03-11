genero = input("Informe o genero: ").upper()
subgenero = input("Informe o subgenero: ").upper()

if (genero == "INVESTIGATIVA"):
	if(subgenero == "SUSPENSE"):
		print("DEXTER")
	elif(subgenero == "DRAMA"):
		print("NARCOS")
	else:
		print("SERIE NAO IDENTIFICADA")
elif(genero == "DRAMATICA"):
	if(subgenero == "COM FICCAO"):
		print("LOST")
	elif(subgenero == "AVENTURA"):
		print("SHERLOCK")
	else:
		print("SERIE NAO IDENTIFICADA")
else:
	print("SERIE NAO IDENTIFICADA")