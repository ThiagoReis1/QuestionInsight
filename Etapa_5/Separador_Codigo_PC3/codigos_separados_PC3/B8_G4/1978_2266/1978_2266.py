e = input().lower()
s = input().lower()
if e != "vertente" and e != "misturado":
	print ("instrumento nao identificado")
else:
	if e == "vertente" :
		if s == "samba-de-raiz":
			print ("cavaquinho")
		elif s == "partido-alto":
			print ("surdo")
		else:
			print ("instrumento nao identificado")
	elif e == "misturado":
		if s == "samba-choro":
			print ("violao de seis cordas")
		elif s == "samba-jazz":
			print ("saxofone")
		else:
			print ("instrumento nao identificado")
			