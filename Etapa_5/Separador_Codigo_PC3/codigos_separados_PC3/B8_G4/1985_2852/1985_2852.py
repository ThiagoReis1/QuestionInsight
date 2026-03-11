r = input(" regiao ").upper()
e = input(" estado ").upper()
if (r == "NORTE" or r == "SUL"):
	if (r == "NORTE"):
		if(e == "AMAZONAS" ):
			print("UNIVERSIDADE FEDERAL DO AMAZONAS")
		elif(e == "RORAIMA"):
			print("UNIVERSIDADE FEDERAL DE RORAIMA")
		else:
			print("UNIVERSIDADE NAO IDENTIFICADA")

	elif (r == "SUL"):
		if (e == "PARANA"):
			print("UNIVERSIDADE FEDERAL DO PARANA")
		elif(e == "SANTA CATARINA"):
			print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
		else:
			print("UNIVERSIDADE NAO IDENTIFICADA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")

	