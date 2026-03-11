X = input("Gênero de série:")
Y = input("Subgênero da série:")
x = (X).upper()
y = (Y).upper()
if((x=="INVESTIGATIVA")or(x=="DRAMATICA")):
	if(x=="INVESTIGATIVA"):
		if(y=="SUSPENSE"):
			z = "DEXTER"
			print(z)
		elif(y=="DRAMA"):
			z = "NARCOS"
			print(z)
		else:
			z="SERIE NAO IDENTIFICADA"
			print(z)
	elif(x=="DRAMATICA"):
		if(y=="COM FICCAO"):
			z = "LOST"
			print(z)
		elif(y=="AVENTURA"):
			z = "SHERLOCK"
			print(z)
		else:
			z="SERIE NAO IDENTIFICADA"
			print(z)
else:
	print("SERIE NAO IDENTIFICADA")