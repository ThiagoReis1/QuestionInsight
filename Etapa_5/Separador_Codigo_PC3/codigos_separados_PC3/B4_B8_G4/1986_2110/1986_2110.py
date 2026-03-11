m = input("Modalidade: ").upper()
t = input("turno: ").upper()

if(m!="BACHARELADO" and m!="LICENCIATURA"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
elif(t!="DIURNO" and t!="VESPERTINO" and t!="NOTURNO"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	
if(m=="BACHARELADO" and t=="DIURNO"):
	print("DIREITO")
elif(m=="BACHARELADO" and t=="NOTURNO"):
	print("ADMINISTRACAO")
elif(m=="LICENCIATURA" and t=="VESPERTINO"):
	print("FILOSOFIA")
elif(m=="LICENCIATURA" and t=="NOTURNO"):
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	

