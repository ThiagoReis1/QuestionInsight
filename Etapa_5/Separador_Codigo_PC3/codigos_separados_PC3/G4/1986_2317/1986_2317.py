m = input("Modalidade: ")
t = input("Turno: ")


if m == "Bacharelado" and t == "Diurno":
	print("DIREITO")
elif m == "Bacharelado" and t == "Noturno":
	print("ADMINISTRACAO")
elif m == "Licenciatura" and t == "Vespertino":
	print("FILOSOFIA")
elif m == "Licenciatura" and t == "Noturno":
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	