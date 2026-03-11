m = input("Modalidade do curso:")
t = input("Turno do Curso:")

if(not(m == "Bacharelado" and m = "Licenciatura"):
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
else:
	if(m.upper() == "BACHARELADO"):
		if(t.upper() == "DIURNO"):
			print("DIREITO")
		elif(m.upper() == "BACHARELADO"):
			if(t.upper() == "NOTURNO"):
				print("ADMINISTRACAO")
		
	if(m.upper() == "LICENCIATURA"):
		if(t.upper() == "VESPERTINO"):
			print("FILOSOFIA")
		elif(m.upper() == "LICENCIATURA"):
			if(t.upper() == "NOTURNO"):
				print("GEOGRAFIA")