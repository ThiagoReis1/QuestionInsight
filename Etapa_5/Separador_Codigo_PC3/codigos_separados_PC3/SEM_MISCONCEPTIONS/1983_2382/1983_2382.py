continente=input()
pais=input()

if(continente!="Asia")and(continente!="America-do-Sul"):
	print("INFORMACAO NAO IDENTIFICADA")
else:
	if(pais!="Jordania")and(pais!="India")and(pais!="Peru")and(pais!="Brasil"):
		print("INFORMACAO NAO IDENTIFICADA")
	else:
		if(continente=="Asia")and(pais!="Jordania")or(pais!="India"):
			print("INFORMACAO NAO IDENTIFICADA")
		else:
			if(continente=="Asia")and(pais=="Jordania"):
				print("as ruinas de petra".upper())
			else:
				if(continente=="Asia")and(pais=="India"):
				print("taj mahal".upper())
			else:
				if(continente=="America-do-Sul")and(pais=="Peru"):
					print("machu picchu".upper())
				else:
					if(continente=="America-do-Sul")and(pais=="Brasil"):
						print("cristo redentor".upper())