g=input("Genero: ").upper()
sg=input("Subgenero: ").upper()

if(g=='INVESTIGATIVA'):
	if(sg=='SUSPENSE'):
		print("DEXTER")
	elif(sg=='DRAMA'):
		print("NARCOS")
	else:
		print("SERIE NAO IDENTIFICADA")
elif(g=='DRAMATICA'):
	if(sg=='COM FICCAO'):
		print("LOST")
	elif(sg=='AVENTURA'):
		print("SHERLOCK")
	else:
		print("SERIE NAO IDENTIFICADA")