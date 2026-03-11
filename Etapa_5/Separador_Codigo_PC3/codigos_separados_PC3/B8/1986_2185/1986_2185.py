modalidade = input("digite modalidade: ")
turno = input("digite turno: ")


if (modalidade.upper() == "BACHARELADO"):
	if(turno.upper() == "DIURNO"):
		print("DIREITO")
	elif(turno.upper() == "NOTURNO"):
		print("ADMINISTRACAO")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")

elif(modalidade.upper() == "LICENCIATURA"):
	if(turno.upper() == "VESPERTINO"):
		print("FILOSOFIA")
	elif(turno.upper() == "NOTURNO"):
		print("GEOGRAFIA")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")


		
		
	