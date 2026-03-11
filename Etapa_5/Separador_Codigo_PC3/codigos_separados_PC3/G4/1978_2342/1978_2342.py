mod1= input().lower()
mod2= input().lower()

if(mod1== "vertente" and mod2=="samba-de-raiz"):
	print("cavaquinho")
elif (mod1=="vertente" and mod2=="partido-alto"):
	print("surdo")
elif (mod1=="misturado" and mod2=="samba-choro"):
	print("violao de seis cordas")
elif (mod1=="misturado" and mod2=="samba-jazz"):
	print("saxofone")
else:
	print("instrumento nao identificado")