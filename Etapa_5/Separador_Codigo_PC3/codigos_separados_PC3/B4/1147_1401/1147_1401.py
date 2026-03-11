personagem = input("Digite o nome da personagem: ")

if(personagem == "Daenerys"):
	pai = "Aegon IV Targaryen"
elif (personagem == "Cersei"):
	pai = "Tywin Lannister"
elif (personagem == "Brienne"):
	pai = "Selwyn Tarth"
elif (personagem == "Arya"):
	pai = "Eddard Stark"
elif (personagem == "Sansa"):
	pai = "Eddard Stark"
elif (personagem == "Margaery"):
	pai = "Garth Tyrell"
elif (personagem == "Catelyn"):
	pai = "Hoster Tully"
elif (personagem == "Meera"):
	pai = "Howland Reed"
else:
	pai = "invalido"
print("Saida: ",pai )	
if(pai == "invalido"):
	print("pai invalido")
