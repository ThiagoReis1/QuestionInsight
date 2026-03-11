a= input("Informe a modalidade")
b= input("Informe o turno")

if(a== "Bacharelado") and (b== "Diurno"):
	print("DIREITO")
elif(a== "Bacharelado") and (b== "Noturno"):
	print("ADMINISTRACAO")
elif(a== "Licenciatura") and (b== "Vespertino"):
	print("FILOSOFIA")
elif(a== "Licenciatura") and (b== "Noturno"):
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
