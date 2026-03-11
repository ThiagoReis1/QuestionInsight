regiao = input()
estado = input()
if(regiao == "Norte") and (estado == "Amazonas"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS".upper())	
elif(regiao == "Norte") and (estado == "Roraima"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA".upper())
elif(regiao == "Sul") and (estado == "Parana"):
	print("UNIVERSIDADE FEDERAL DO PARANA".upper())
elif(regiao == "Sul") and (estado == "Santa Catarina"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA".upper())
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")