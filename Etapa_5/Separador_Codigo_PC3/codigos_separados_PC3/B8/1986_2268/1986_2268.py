Modalidade=input("modalidade: ")
Turno=input("Turno :")
if (Modalidade=="Bacharelado") and (Turno=="Diurno"):
	print("Direito")
elif(Turno=="Noturno") and (Modalidade=="Bacharelado"):
	nome="administração"
	print(nome.upper())
	
else:
	if(Modalidade=="Licenciatura") and (Turno=="Vespertino"):
		nome1="filosofia"
		print(nome1.upper())
	if (Turno=="Noturno") and (Modalidade=="Licenciatura"):
		nome2="geografia"
		print(nome2.upper())
		
	