a = input().lower()
b = input().lower()


if("vertente" == a):
	if("samba-de-raiz" == b):
	   print("cavaquinho")
	elif("partido-alto" == b):
		print("surdo")
	else:
		print("instrumento nao identificado")
else:
	if("misturado" == a):
		if("samba-choro" == b):
			print("violao de seis cordas")
		elif("samba-jazz" == b):
			print("saxofone")
		else:
			print("instrumento nao identificado")
	else:
		print("instrumento nao identificado")
	

	