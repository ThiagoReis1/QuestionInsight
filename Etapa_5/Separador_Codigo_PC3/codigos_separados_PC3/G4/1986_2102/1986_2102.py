mod1= input().upper()
mod2=input().upper()

if(mod1== "BACHARELADO" and mod2== "DIURNO"):
	print("DIREITO")
elif(mod1== "BACHARELADO" and mod2=="NOTURNO"):
	print("ADMINISTRACAO")
elif(mod1== "LICENCIATURA" and mod2=="VESPERTINO"):
	print("FILOSOFIA")
elif(mod1== "LICENCIATURA" and mod2=="NOTURNO"):
	print("GEOGRAFIA")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")