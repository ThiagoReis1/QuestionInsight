G=input()
S=input()
A= G.lower();
B= S.lower();
if(A!='vertente' and A!='misturado'):
	print("instrumento nao identificado")
else:
	if(A=='vertente' and B=='samba-de-raiz'):
		print("cavaquinho")
	elif(A=='vertente' and B=="partido-alto"):
		print("surdo")
	elif(A=='misturado' and B=='samba-choro'):
		print("violao de seis cordas")
	elif(A=='misturado' and B=='samba-jazz'):
		print("saxofone")
	else:
		print("instrumento nao identificado")