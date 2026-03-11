c = input("Regiao do pais: ")
p = input("Estado: ")

if(c == "Norte" and p == "Amazonas"):
	print("UNIVERSIDADE FEDERAL DO AMAZONAS")
elif(c== "Norte" and p =="Roraima"):
	print("UNIVERSIDADE FEDERAL DE RORAIMA")
elif(c=="Sul" and p =="Parana"):
	print("UNIVERSIDADE FEDERAL DO PARANA")
elif(c=="Sul" and p=="Santa Catarina"):
	print("UNIVERSIDADE FEDERAL DE SANTA CATARINA")
else: 
	print("UNIVERSIDADE NAO IDENTIFICADA")
    