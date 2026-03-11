r = input("digite regiao: ")
e = input("digite o estado: ")

if(r == "norte" and e == "amazonas"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif(r == "norte" and e == "roraima"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif(r == "sul" and e == "parana"):
	print("UNIVERSIDADE FEDERAL DO PARANA")
elif(r == "sul" and e == "santa catarina"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")

else:
	print("UNIVERSIDADE NAO IDENTIFICADA")