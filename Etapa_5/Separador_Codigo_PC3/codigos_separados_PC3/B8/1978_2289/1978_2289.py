genero = input("qual eh o genero? ").lower()
subgenero = input("qual eh o subgenero? ").lower()

if (genero != "Vertente" and genero != "Misturado"):
	print("instrumento nao identificado")
else:
	if (genero == "Vertente" and subgenero == "Samba-de-raiz"):
		print("cavaquinho")
	elif(genero == "Vertente" and subgenero == "Partido-alto"):
		print("surdo")
	elif (genero == "Misturado" and subgenero == "Samba-choro"):
		print("violado de seis cordas")
	elif (genero == "Misturado" and subgenero == "Samba-jazz"):
		print("saxofone")
 