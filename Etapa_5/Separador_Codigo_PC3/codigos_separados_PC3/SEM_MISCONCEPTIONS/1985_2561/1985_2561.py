regiao = input().upper()
estado = input().upper()
regiao = regiao.upper()
estado = estado.upper()

if (regiao == "NORTE" and estado == "AMAZONAS"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif (regiao == "NORTE" and estado == "RORAIMA"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif (regiao == "SUL" and estado == "PARANA"):
	print("UNIVERSIDADE FEDERAL DO PARANA")
elif (regiao == "SUL" and estado == "SANTA CATARINA"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")