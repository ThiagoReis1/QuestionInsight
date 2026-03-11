caracteristica1 = input("Modalidade").upper()
caracteristica2 = input("Turno").upper()

if((caracteristica1 == "BACHARELADO") and (caracteristica2 == "DIURNO")):
	print("DIREITO")
elif((caracteristica1 == "BACHARELADO") and (caracteristica2 =="NOTURNO")):
	print("ADMINISTRACAO")
elif((caracteristica1 == "LICENCIATURA") and(caracteristica2 == "VESPERTINO")):
	print("FILOSOFIA")
elif((caracteristica1 =="LICENCIATURA") and (caracteristica2 == "NOTURNO")):
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")