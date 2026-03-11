mod= input("modalidade:")
t= input("turno:")

if  (mod.lower() != "bacharelado") and(mod.lower() != "licenciatura"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
elif  (t.lower() != "diurno") and (t.lower() != "noturno") and(t.lower()!= "vespertino"):
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")
elif  (mod.lower() == "bacharelado") and (t.lower() == "diurno"):
	c= "Direito"
	print(c.upper())
elif  (mod.lower() == "bacharelado") and (t.lower() == "noturno"):
	c= "Administracao"
	print(c.upper())
elif  (mod.lower() == "licenciatura") and(t.lower() == "vespertino"):
	c= "filosofia"
	print(c.upper())
elif  (mod.lower() == "licenciatura") and(t.lower() == "noturno"):
	c="geografia"
	print(c.upper())
else:
	print("CURSO DE GRADUACAO NAO IDENTIFICADO")



	