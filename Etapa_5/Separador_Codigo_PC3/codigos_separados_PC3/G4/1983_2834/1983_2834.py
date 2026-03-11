c = input("nome do continente: ")
p = input("nome do pais: ")

#if(((c == "Asia") or (c == "America-do-Sul")) and ((p == "Jordania") or (p == "India") or (p == "Peru") or (p == "Brasil"))):
	
if((c == "Asia") and (p == "Jordania")):
		#print("AS RUINAS DE PETRA")
	print("as ruinas de petra".upper())	
elif((c == "Asia") and (p == "India")):
		#print("TAJ MAHAL")
	print("taj mahal".upper())
elif((c == "America-do-Sul") and (p == "Peru")):
		#print("MACHU PICCHU")
	print("machu picchu".upper())
elif((c == "America-do-Sul") and (p == "Brasil")):
		#print("CRISTO REDENTOR")
	print("cristo redentor".upper())
else:
	print("INFORMACAO NAO IDENTIFICADA")