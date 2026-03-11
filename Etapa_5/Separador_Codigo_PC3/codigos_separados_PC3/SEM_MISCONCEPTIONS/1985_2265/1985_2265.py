Regiao_do_pais = input("Digite a regiao:")
Estado = input("Digite o estado:")

if((Regiao_do_pais.upper() != "Norte") and (Estado.upper() != "Amazonas")):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
														 
elif((Regiao_do_pais.upper() != "Norte") and (Estado.upper()  != "Roraima")):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")

elif((Regiao_do_pais.upper() != "Sul") and (Estado.upper() != "Parana")):
	print("UNIVERSIDADE FEDERAL DO PARANA")

elif((Regiao_do_pais.upper() != "Sul") and (Estado.upper() != "Santa Catarina")):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
	
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")

	



	
