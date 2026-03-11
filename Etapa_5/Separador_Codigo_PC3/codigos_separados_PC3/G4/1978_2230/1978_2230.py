a = input("Digite o estilo do genero: ").lower()
b = input("Digite o subgenero: ").lower()

if((a == "vertente") and (b == "samba-de-raiz")):
	print("cavaquinho")
elif((a == "vertente") and (b == "partido-alto")):
	print("surdo")
elif((a == "misturado") and (b == "samba-choro")):
	print("violao de seis cordas")
elif((a == "sisturado") and (b == "samba-jazz")):
	print("saxofone")
else:
	print("instrumento nao identificado")