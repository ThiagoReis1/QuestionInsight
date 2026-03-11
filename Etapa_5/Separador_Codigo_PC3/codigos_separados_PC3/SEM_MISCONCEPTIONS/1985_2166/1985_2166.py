regiao= input("Regiao situada: ")
estado= input("Estado situada: ")
if(regiao.upper()=="SUL" and estado.upper()=="SANTA CATARINA"):
		print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")

elif(regiao.upper()=="NORTE" and estado.upper()=="RORAIMA"):
		print("UNIVERSIDADE FEDERAL DE RORAIMA")			
elif(regiao.upper()=="NORTE" and estado.upper()=="AMAZONAS"):
		print("UNIVERSIDADE FEDERAL DO AMAZONAS")		
	
elif(regiao.upper()=="SUL" and estado.upper()=="PARANA"):
		print("UNIVERSIDADE FEDERAL DO PARANA")
		
else:
	print("UNIVERSIDADE NAO IDENTIFICADA")