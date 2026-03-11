est = input("Estilo musical:").lower()
sub = input("Subgênero musical:").lower()

if (est!="misturado")and(est!="vertente"):
	print("instrumento nao identificado")
elif (sub!="samba-de-raiz")and(sub!="partido-alto")and(sub!="samba-choro")and(sub!="samba-jazz"):
	print("instrumento nao identificado")
else:
	if (est=="vertente")and((sub=="samba-de-raiz")or(sub=="partido-alto")):
		if(sub=="samba-de-raiz"):
			print("cavaquinho")
		else:
			print("surdo")
	elif(est=="misturado")and((sub=="samba-choro")or(sub=="samba-jazz")):
		if(sub=="samba-choro"):
			print("violao de seis cordas")
		else:
			print("saxofone")	
	else:
		print("instrumento nao identificado")
		
			
		