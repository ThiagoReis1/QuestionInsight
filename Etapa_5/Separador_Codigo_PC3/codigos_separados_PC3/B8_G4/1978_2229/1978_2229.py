#entrada
E=input("Seu estilo: ").lower()
S=input("subgenero: ").lower()
#condicao
if(E=="vertente") or (E=="misturado"):
	if(E=="vertente")and(S=="samba-de-raiz"):	
		print("cavaquinho")
	elif(E=="vertente")and(S=="partido-alto"):
		print("surdo")
	elif(E=="misturado")and(S=="samba-choro"):
		print("violao de seis cordas")
	elif(E=="misturado")and(S=="samba-jazz"):
		print("saxofone")
else:
	print("instrumento nao identificado")
