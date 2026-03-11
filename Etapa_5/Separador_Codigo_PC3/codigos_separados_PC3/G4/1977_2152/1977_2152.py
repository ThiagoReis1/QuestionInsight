x = input("genero da serie:" ).upper()
y = input("subgenero da serie:" ).upper()

if((x=="INVESTIGATIVA") and (y=="SUSPENSE")):
		print("DEXTER")
elif((x=="INVESTIGATIVA") and (y=="DRAMA")):
		print("NARCOS")
elif((x=="DRAMATICA") and (y=="COM FICCAO")):
		print("LOST")
elif((x=="DRAMATICA") and (y=="AVENTURA")):
		print("SHERLOCK")
else:
	print("SERIE NAO IDENTIFICADA")