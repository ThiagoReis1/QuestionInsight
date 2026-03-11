#Personagem mulher de a guerra dos tronos (pm)
pm=input("Nome da personagem:")

#Validacao
if((pm=="Daenerys")or(pm=="Cersei")or(pm=="Brienne")or(pm=="Arya")or(pm=="Sansa")or(pm=="Margaery")or(pm=="Catelyn")or(pm=="Meera")):
	if(pm=="Daenerys"):
		nome="Aegon IV Targaryen"
	elif(pm=="Cersei"):
		 nome="Tywin Lannister"
	elif(pm=="Brienne"):
		nome="Selwyn Tarth"
	elif(pm=="Arya"):
		nome="Eddard Stark"
	elif(pm=="Sansa"):
		nome="Eddard Stark"
	elif(pm=="Margaery"):
		nome="Garth Tyrell"
	elif(pm=="Catelyn"):
		nome="Hoster Tully"
	elif(pm=="Meera"):
		nome="Howland Reed"
	print(nome)
else:
	print("Entrada ", pm , "invalida")