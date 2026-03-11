x= input().upper()
y= input().upper()

#if((x=="NORTE") and (y =="RORAIMA")):
#	print("UNIVERSIDADE FEDERAL DE RORAIMA")
#elif((x=="NORTE") and (y =="AMAZONAS")):
#	print("UNIVERSIDADE FEDERAL DO AMAZONAS")	
#elif ((x == "SUL" ) and (y == "SANTA CATARINA")):
#	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
#elif((x == "SUL" ) and (y == "PARANA")):
#		print("UNIVERSIDADE FEDERAL DO PARANA")
#else:
#	print("UNIVERSIDADE NAO IDENTIFICADA")
if((x=="NORTE") and (y=="AMAZONAS")):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif((x=="NORTE") and (y=="RORAIMA")):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif((x=="SUL") and (y=="SANTA CATARINA")):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
elif((x=="SUL") and (y=="PARANA")):
	print("UNIVERSIDADE FEDERAL DO PARANA")
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")