r = input("Regiao do Pais: ")
e = input("Qual o Estado?: ")

if (r != "Norte") and (r != "Sul") or (e != "Amazonas") and (e != "Roraima") and (e != "Parana") and (e != "Santa Catarina"):
	print("UNIVERSIDADE NAO IDENTIFICADA")
	
elif (r == "Norte") and (e == "Amazonas"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
	
elif (r == "Norte") and (e == "Roraima"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
	
elif(r == "Sul") and (e == "Parana"):
	print("UNIVERSIDADE FEDERAL DO PARANA")
	
elif (r == "Sul") and (e == "Santa Catarina"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
	
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")