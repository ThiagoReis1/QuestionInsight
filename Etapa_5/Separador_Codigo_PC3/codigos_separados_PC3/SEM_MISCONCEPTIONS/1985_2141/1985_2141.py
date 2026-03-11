regiao = input("").upper()
estado = input("").upper()

if((regiao == "NORTE") and (estado == "AMAZONAS")):
	x = "UNIVERSIDADE FEDERAL DO AMAZONAS"
	print(x)
elif((regiao == "NORTE") and (estado == "RORAIMA")):
	x = "UNIVERSIDADE FEDERAL DE RORAIMA"
	print(x)
elif((regiao == "SUL") and (estado == "PARANA")):
	x = "UNIVERSIDADE FEDERAL DO PARANA"
	print(x)
elif((regiao == "SUL") and (estado == "SANTA CATARINA")):
	x = "UNIVERSIDADE FEDERAL DE SANTA CATARINA"
	print(x)
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")