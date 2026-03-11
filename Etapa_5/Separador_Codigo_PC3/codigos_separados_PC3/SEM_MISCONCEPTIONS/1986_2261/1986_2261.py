mod = input("modalidade:").upper()
turno = input("turno:").upper()

if((mod == "BACHARELADO") and (turno == "DIURNO")):
	x = "direito".upper()
	print(x)
elif((mod == "BACHARELADO") and (turno == "NOTURNO")):
	x = "administracao".upper()
	print(x)
elif((mod == "LICENCIATURA") and (turno == "VESPERTINO")):
	x = "Filosofia".upper()
	print(x)
elif((mod == "LICENCIATURA") and (turno == "NOTURNO")):
	x = "geografia".upper()
	print(x)
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")