estilo = input("informe o estilo musical:")
sub = input("informe o subgenero:")

if(estilo == "Vertente") and (sub == "Samba-de-raiz"):
	print("cavaquinho")
elif(estilo == "Vertente") and (sub == "Partido-alto"):
	print("surdo")
elif(estilo == "Misturado") and (sub == "Samba-choro"):
	print("violao de seis cordas")
elif(estilo == "Misturado") and (sub == "Samba-jazz"):
	print("saxofone")
else:
	print("instrumento nao identificado")
	