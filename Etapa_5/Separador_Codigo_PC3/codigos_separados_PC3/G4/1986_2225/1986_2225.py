m=input("Bacharelado ou Licenciatura? ").upper()
t=input("Diurno, Noturno ou Vespertino? ").upper()
	
if(m=="BACHARELADO" and t=="DIURNO"):
	x= "DIREITO"
	print(x)
elif(m=="BACHARELADO" and t=="NOTURNO"):
	x="ADMINISTRACAO"
	print(x)
elif(m=="LICENCIATURA" and t=="VESPERTINO"):
	x="FILOSOFIA"
	print(x)
elif(m=="LICENCIATURA" and t=="NOTURNO"):
	x="GEOGRAFIA"
	print(x)
	
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")