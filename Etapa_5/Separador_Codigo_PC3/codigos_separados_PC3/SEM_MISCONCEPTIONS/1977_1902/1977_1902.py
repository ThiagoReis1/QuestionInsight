genero=input(":").upper()
subgenero=input(":").upper()
if(genero=="INVESTIGATIVA" and subgenero=="SUSPENSE"):
	print("DEXTER")
elif(genero=="INVESTIGATIVA" and subgenero=="DRAMA"):
	print("NARCOS")
elif(genero=="DRAMATICA" and subgenero=="COM FICCAO"):
	print("LOST")
elif(genero=="DRAMATICA" and subgenero=="AVENTURA"):	
	print("SHERLOCK")
else:
	print("SERIE NAO IDENTIFICADA")