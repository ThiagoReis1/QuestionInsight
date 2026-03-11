regiao = input("digite regiao: ")
estado = input("digite estado: ")

if	(regiao != "norte") and (estado.upper() != "AMAZONAS") and (estado != "RORAIMA"):
	if	(regiao != "sul") and (estado != "PARANA") and (estado != "SANTA CATARINA"):
		print("UNIVERSIDADE NAO IDENTIFICADA")
else:
	if regiao == "norte" and estado == "Amazonas":
		valor = "Amazonas"
		else:
			valor = "Roraima"
			print(valor)
			
	elif regiao == "sul" and estado == "Santa Catarina":
			valor == "Santa Catarina"
		else:
			valor = "Parana"
			print(valor)
	
																			 

