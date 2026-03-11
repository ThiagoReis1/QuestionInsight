regiao = input () .upper()
estado = input () .upper()
regiao = "norte"

if (regiao != "norte" and regiao != "sul" or estado != 
	 print ("UNIVERSIDADE NAO IDENTIFICADA.")
else:
	if (regiao == "norte" and estado == "amazonas"):
		print ("UNIVERSIDADE FEDERAL DO AMAZONAS")
	elif (regiao == "norte" and estado == "roraima"):
		print ("UNIVERSIDADE FEDERAL DE RORAIAMA")
	elif (regiao == "sul" and estado == "parana"):
		print ("UNIVERSIDADE FEDERAL DE PARANÁ")
	elif (regiao == "sul" and estado == "SANTA CATARINA"):
		print ("UNIVERSIDADE FEDERAL DE SANTA CATARINA")

		

