r_pais = input("Insira a Regiao do pais: ").upper()
estado = input("Insira o estado: ").upper()

if(r_pais == "NORTE") or (r_pais == "SUL"):
	if(r_pais == "NORTE") and (estado == "AMAZONAS"):
		print("UNIVERSIDADE FEDERAL DO AMAZONAS")
	elif(estado == "RORAIMA") and (r_pais == "SUL"):
		print("UNIVERSIDADE FEDERAL DE RORAIMA")
	elif(r_pais == "SUL") and (estado == "PARANA"):
		print("UNIVERSIDADE FEDERAL DO PARANA")
	elif(r_pais == "SUL") and (estado == "SANTA CATARINA"):
		print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")