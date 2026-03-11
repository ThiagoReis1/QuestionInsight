regiao = input("Informe a regiao do pais: ")
estado = input("Informe qual o estado: ")
x = regiao.upper()
y = estado.upper()

if (x == "NORTE"and y=="AMAZONAS" ):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif (x == "NORTE" and y == "RORAIMA"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif (x == "SUL" and y=="PARANA" ):
	print("UNIVERSIDADE FEDERAL DO PARANA")
elif (y == "SANTA CATARINA" and x=="SUL"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")
