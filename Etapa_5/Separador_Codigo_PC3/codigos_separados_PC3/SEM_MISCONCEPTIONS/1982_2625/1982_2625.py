pais = input(" ")
cidade = input(" ")

if((pais == "Italia" or pais == "Espanha")and(cidade == "Roma" or cidade=="Florenca" or cidade == "Frigiliana" or cidade == "Madrid")):
	if(pais == "Italia" and cidade == "Roma"):
	   print("LATINA")
	elif(pais == "Italia" and cidade == "Florenca"):
		print("SIENA")
	elif(pais == "Espanha" and cidade == "Frigiliana"):
		print("MALAGA")
	elif(pais == "Espanha" and cidade == "Madrid"):
		print("MADRID")
	else:
		print("PROVINCIA NAO IDENTIFICADA")
else:
	print("PROVINCIA NAO IDENTIFICADA")
	  
