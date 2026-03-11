estilo = input("instrumento: ")
sub = input("subgenero: ")
if(estilo == "Vertente") or (estilo == "Misturado"):
	if(estilo == "Vertente"):
		if sub == "Samba-de-raiz":
			print("cavaquinho")
		else:
			print("surdo")
	else:
		if sub == "Samba-choro":
			print("violao de cordas")
		elif sub == "samba-jazz":	
			print("saxofone")
else:
	print("instrumento nao identificado")
			