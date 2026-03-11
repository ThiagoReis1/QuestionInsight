
r = input("regiao: ").upper()
e = input("estado: ").upper()

if(r == "NORTE" and e == "AMAZONAS"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif(r== "NORTE" and e =="RORAIMA"):
   print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif(r=="SUL" and e =="PARANA"):
   print("UNIVERSIDADE FEDERAL DO PARANA")
elif(r=="SUL" and e =="SANTA CATARINA"):
   print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
else: 
    print("UNIVERSIDADE NAO IDENTIFICADA")
