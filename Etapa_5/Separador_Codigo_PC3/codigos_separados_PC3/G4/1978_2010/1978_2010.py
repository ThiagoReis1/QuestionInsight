c1=(input("estilo do gênero músical: ")).lower()
c2=(input("subgênero musica: ")).lower()

if(c1 == "vertente") and ((c2 == "samba-de-raiz") or (c2 == "partido-alto")):
	if(c2 == "samba-de-raiz"):
		print("cavaquinho")
	else:
		print("surdo")
elif(c1 == "misturado" ) and ((c2 == "samba-choro") or (c2 == "samba-jazz")):
	if(c2 == "samba-choro"):
		print("violao de seis cordas")
	else:
		print("saxofone")
else:
	print("instrumento nao identificado")