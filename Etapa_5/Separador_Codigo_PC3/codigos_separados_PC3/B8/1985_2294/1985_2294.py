regiao = input("regiao do pais: ").upper()
estado = input("estado da regiao: ").upper()
if(regiao != str("Norte") and regiao != str("Sul")) and (estado != str("Amazonas") and estado != str("Roraima") and estado != str("Parana") and estado != str("Santa Catarina")):
	print("UNIVERSIDADE NAO IDENTIFICADA")
elif (regiao == str("Norte")):
	if (estado == str("Amazonas")):
		print("UNIVERSIDADE FEDERAL DO AMAZONAS")
	if(estado == str("Roraima")):
		print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif (regiao == str("Sul")):
	if(estado == str("Parana")):
		print("UNIVERSIDADE FEDERAL DO PARANA")
	if(estado == str("Santa Catarina")):
		print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
