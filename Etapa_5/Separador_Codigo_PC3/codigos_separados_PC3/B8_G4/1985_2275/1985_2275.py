r = input("regiao do pais: ")
e = input("estado: ")

if not( r == "Norte") and not( r == "Sul") and not(e == "Parana") and not( e == "Santa Catarina"):
	print("UNIVERSIDADE NAO IDENTIFICADA")
elif( r == "Norte") and ( e == "Amazonas"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif( r == "Norte" ) and ( e == "Roraima"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif( r == "Sul") and ( e == "Parana"):
	print("UNIVERSIDADE FEDERAL DO PARANA")
elif( r == "Sul") and (e == "Santa Catarina"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")