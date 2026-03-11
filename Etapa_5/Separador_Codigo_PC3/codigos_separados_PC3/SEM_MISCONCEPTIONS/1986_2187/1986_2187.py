modal = input("Modalidade: ")
turno = input("Turno: ")

if(modal.upper() == "BACHARELADO"):
	if(turno.upper() == "DIURNO"):
		print("DIREITO")
	elif(turno.upper() == "NOTURNO"):
		print("ADMINISTRACAO")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")

elif(modal.upper() == "LICENCIATURA"):
	if(turno.upper() == "VESPERTINO"):
		print("FILOSOFIA")
	elif(turno.upper() == "NOTURNO"):
		print("GEOGRAFIA")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")

else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")