modalidade = input("Digite a modalidade: ")
if(modalidade.upper() != "BACHARELADO" and modalidade.upper() != "LICENCIATURA"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	
else:
	turno = input("Digite o turno: ")
	if(turno.upper() != "DIURNO" and turno.upper() != "NOTURNO" and turno.upper() != "VESPERTINO"):
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	
	elif(modalidade.upper() == "BACHARELADO"):
			if(turno.upper() == "DIURNO"):
				print("DIREITO")
			else:
				prit("ADMINISTRACAO")
	else:
		if(turno.upper() == "VESPERTINO"):
			print("FILOSOFIA")
		else:
			print("GEOGRAFIA")
		