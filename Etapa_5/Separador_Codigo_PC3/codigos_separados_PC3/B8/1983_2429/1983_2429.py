
continente = input("qual continente: ")
pais = input("qual pais: ")

if((continente == "Asia") or (continente == "America-do-Sul")):
	if (continente == "Asia"):
		if(pais == "Jordania" or pais == "India"):
			if (pais == "Jordania"):
				print("as ruinas de petra".upper())
			elif (pais == "India"):
				print("TAJ MAHAL".upper())
		else:
			print("INFORMACAO NAO IDENTIFICADA")
	else:
		if(continente == "America-do-Sul"):
			if(pais == "Peru" or pais == "Brasil"):
				if(pais == "Peru"):
					print("MACHU PICCHU".upper())
				elif(pais == "Brasil"):
					print("CRISTO REDENTOR".upper())
			else:
				print("INFORMACAO NAO IDENTIFICADA")
else:
	print("INFORMACAO NAO IDENTIFICADA".upper())
		
		