m = input().upper()
t = input().upper()

if m == "BACHARELADO" or t == "LICENCIATURA" and (t == "DIURNO" or t == "NOTURNO" or t == "VESPERTINO"):
	if m == "BACHARELADO":
		if t== "DIURNO":
			print("DIREITO")
		elif t== "NOTURNO":
			print("ADMINISTRACAO")
		else:
			print("CURSO DE GRADUACAO NAO IDENTIFICADO")
	elif m == "LICENCIATURA":
		if t == "VESPERTINO":
			print("FILOSOFIA")
		elif t == "NOTURNO":
			print("GEOGRAFIA")
		else:
			print("CURSO DE GRADUACAO NAO IDENTIFICADO")
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")