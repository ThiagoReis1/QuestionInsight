modalidade = input(("Modalidade: "))
turno = input(("Turno: "))

if(modalidade == "Bacharelado") and (turno == "Diurno"):
	print("Direito".upper())
elif(modalidade == "Bacharelado") and (turno == "Noturno"):
	print("Administracao".upper())
elif(modalidade == "Licenciatura") and (turno == "Vespertino"):
	print("Filosofia".upper())
elif(modalidade == "Licenciatura") and (turno == "Noturno"):
	print("Geografia".upper())
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")