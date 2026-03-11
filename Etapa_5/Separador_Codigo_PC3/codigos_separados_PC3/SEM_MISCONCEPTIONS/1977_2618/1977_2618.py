genero= input("Genero: ")
subgenero= input("subgenero: ")
if(genero.upper() == "INVESTIGATIVA"):
	if(subgenero.upper() == "SUSPENSE"):
		print("DEXTER")
	elif(subgenero.upper() == "DRAMA"):
		print("NARCOS")
	else:
		print("SERIE NAO IDENTIFICADA")
elif(genero.upper() == "DRAMATICA"):
	if(subgenero.upper() == "COM FICCAO"):
		print("LOST")
	elif(subgenero.upper() == "AVENTURA"):
			print("SHERLOCK")
	else:
			print("SERIE NAO IDENTIFICADA")
else:
	print("SERIE NAO IDENTIFICADA")
	
			

			