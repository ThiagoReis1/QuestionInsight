modalidade = input("modalidade: ")
turno = input("turno: ")

if (modalidade == "Bacharelado" and turno == "Diurno"):
	print("DIREITO")
	
elif (modalidade == "Bacharelado" and turno == "Noturno"):
	print("ADMINISTRACAO")
	
elif (modalidade == "Licenciatura" and turno == "Vespertino"):
	print("FILOSOFIA")
	
elif (modalidade == "Licenciatura" and turno == "Noturno"):
	print("GEOGRAFIA")
	
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")