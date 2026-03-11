regiao = input("Norte/Sul: ")
estado = input("Qual estado: ")
if((regiao == "norte") or (regiao == "sul")):
	if((estado =="amazonas") or (estado =="roraima") or (estado =="parana") or (estado =="santa catarina")):
		if(regiao=="norte" and estado=="amazonas"):
			unn = ("Universidade federal do amazonas")
		elif(regiao=="norte" and estado=="roraima"):
			unn = ("Universidade federal de roraima")
		elif(regiao=="sul" and estado=="parana"):
			unn = ("Universidade federal do parana")
		else:
			unn = ("Universidade federal de santa catarina")
		print(unn.upper())
	else:
		print("UNIVERSIDADE NAO IDENTIFICADA.")	
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")
	