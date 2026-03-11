m = input("Modalidade:")
t = input("Turno:")
m = m.upper()
t = t.upper()

if(m=="BACHARELADO"):
	if(t=="DIURNO"):
		print("DIREITO")
	elif(t=="NOTURNO"):
		print("ADMNISTRACAO")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
elif(m=="LICENCIATURA"):
	if(t=="VESPERTINO"):
		print("FILOSOFIA")
	elif(t=="NOTURNO"):
		print("GEOGRAFIA")
	else:
		print("CURSO DE GRADUACAO NAO IDENTIFICADO")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
			