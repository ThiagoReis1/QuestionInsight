gen = input()
subgen = input()

if (gen.lower() == "vertente"):
	if (subgen.lower() == "samba-de-raiz"):
		inst = "cavaquinho"
	elif (subgen.lower() == "partido-alto"):
		inst = "surdo"
	else:
		inst = "instrumento nao identificado"

elif (gen.lower() == "misturado"):
	if (subgen.lower() == "samba-choro"):
		inst = "violao de seis cordas"
	elif (subgen.lower() == "samba-jazz"):
		inst = "saxofone"
	else:
		inst = "instrumento nao identificado"
		
else:
	inst = "instrumento nao identificado"
		
print (inst)