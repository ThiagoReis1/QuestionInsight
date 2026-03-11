#Entrada do estilo musical
x = input("Entre com o estilo musical: ").lower()

#Entrada do subgenero musical
y = input("Entre com o subgenero musical: ").lower()

if ((x != "vertente") and (x != "misturado")) or ((y != "samba-de-raiz") and (y != "partido-alto") and (y != "samba-choro") and (y != "samba-jazz" )):
	print("instrumento nao identifcado.")
elif (x == "vertente") and (y == "samba-de-raiz"):
	print("cavaquinho")
elif (x == "vertente") and (y == "partido-alto"):
	print("surdo")
elif (x == "misturado") and (y == "samba-choro"):
	print("violao de seis cordas")
elif (x == "misturado") and (y == "samba-jazz"):
	print("saxofone")

