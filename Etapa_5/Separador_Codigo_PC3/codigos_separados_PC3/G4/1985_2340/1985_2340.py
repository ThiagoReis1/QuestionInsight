#leia duas características que definem uma universidade apenas das regiões Norte e Sul
#como saída, o programa deve identificar e imprimir o nome da universidade

reg = input("Região Norte ou Sul: ").upper()
uf = input("Estado: ").upper()

if (reg == "norte") or (reg == "NORTE"):
	if (uf == "amazonas") or (uf == "AMAZONAS"):
		print("UNIVERSIDADE FEDERAL DO AMAZONAS")
	elif (uf == "roraima") or (uf == "RORAIMA"):
		print("UNIVERSIDADE FEDERAL DE RORAIMA")
	else:
		print("UNIVERSIDADE NAO IDENTIFICADA")
elif (reg == "sul") or (reg == "SUL"):
	if(uf == "parana") or (uf == "PARANA"):
		print("UNIVERSIDADE FEDERAL DO PARANA")
	elif(uf == "santa catarina") or ("SANTA CATARINA"):
		print("UNIVERSIDADE FEDERAL DE SANTA CARARINA")
	else:
		print("UNIVERSIDADE NAO IDENTIFICADA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")