mod= input("digite a modalidade do curso: ")
tur= input("digite o turno do curso: ")

if(mod.upper() == "bacharelado"):
	if(tur.upper()== "diurno"):
		print("DIREITO")
	elif(tur.upper() == "noturno"):
		print("ADMINISTRAÇÃO")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
if(mod.upper() == "Licenciatura"):
	if(tur.upper() =="vespertino"):
		print("FILOSOFIA")
	elif(tur.upper() == "noturno"):
		print("GEOGRAFIA")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
			