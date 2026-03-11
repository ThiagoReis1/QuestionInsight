m = input("modalidade: ")
t = input("turno: ")

if (m.upper() == "BACHARELADO"):
	if(t.upper() == "DIURNO"):
		print("DIREITO")
	elif(t.upper() == "NOTURNO"):
		print("ADMINISTRACAO")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
elif(m.upper() == "LICENCIATURA"):
	if(t.upper() == "VESPERTINO"):
		print("FILOSOFIA")
	elif(t.upper() == "NOTURNO"):
		print("GEOGRAFIA")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")	