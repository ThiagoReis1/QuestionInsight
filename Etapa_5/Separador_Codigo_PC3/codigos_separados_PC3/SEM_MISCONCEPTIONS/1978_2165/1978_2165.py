estilo = input()
sub = input()

if(estilo.lower() == "Vertente"):
	if(sub.lower() == "samba-de-raiz"):
		print("cavaquinho")
	else:
		print("surdo")
elif(estilo.lower() == "Misturado"):
	if(sub.lower() == "Samba-choro"):
		print("violao de seis cordas")
	else:
		print("saxofone")
else:
	print("instrumento nao identificado.")
