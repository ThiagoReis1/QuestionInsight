X = input("Estilo do gênero musical:").lower()
Y = input("O subgênero musical:").lower()

if ((X == "vertente") and (Y == "samba-de-raiz")):
	print("cavaquinho")
elif ((X == "vertente") and (Y == "partido-alto")):
	print("surdo")
elif ((X == "misturado") and (Y == "samba-choro")):
	print("violao de seis cordas")
elif ((X == "misturado") and (Y == "samba-jazz")):
	print("saxofone")
else:
	print("instrumento nao identificado")