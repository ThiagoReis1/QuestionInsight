m=input("modalidade:")
t=input("turno:")
if (m.upper!="BACHARELADO") and (m.upper()!= "LICENCIATURA") and (t.upper()!="DIURNO") and (t.upper()!="NOTURNO") and (t.upper()!="VESPERTINO"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
else:
	if (m.upper()=="BACHARELADO") and (t.upper()=="DIURNO"):
		print("DIREITO")
	elif (m.upper()=="BACHARELADO") and (t.upper()=="NOTURNO"):
		print("ADMINISTRACAO")
	elif (m.upper()=="LICENCIATURA") and (t.upper()=="VESPERTINO"):
		print("FILOSOFIA")
	else:
		print("GEOGRAFIA")