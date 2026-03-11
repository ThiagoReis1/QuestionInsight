m= input("Modalidade: ").upper()
t= input("Turno: ").upper()

if(m == "BACHARELADO" and t == "DIURNO"):
	a = "Direito"
	print(a.upper())
else:
	if(m == "BACHARELADO" and t == "NOTURNO"):
		b= "administracao"
		print(b.upper())
	else:
		if(m == "LICENCIATURA" and t == "VESPERTINO"):
			c= "filosofia"
			print(c.upper())
		else:
			if(m== "LICENCIATURA" and t == "NOTURNO"):
				d= "geografia"
				print(d.upper())
			else:
				print("CURSO DE GRADUACAO NAO IDENTIFICADO")
				
		


	
	