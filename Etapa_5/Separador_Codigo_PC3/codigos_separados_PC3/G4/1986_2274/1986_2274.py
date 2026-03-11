x = input("Modalidade:").upper()
y = input("Turno:").upper()

if ((x == "BACHARELADO") and (y == "DIURNO")):
	print("DIREITO")
elif ((x == "BACHARELADO") and (y == "NOTURNO")):
	print("ADMINISTRACAO")
elif ((x == "LICENCIATURA") and (y == "VESPERTINO")):
	print("FILOSOFIA")
elif ((x == "LICENCIATURA") and (y == "NOTURNO")):
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
   
