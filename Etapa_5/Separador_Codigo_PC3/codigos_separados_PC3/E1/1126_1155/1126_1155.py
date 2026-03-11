stark=input("digite o nome do stark")
if(stark=="Sansa"):
	lobo="Lady"
elif(stark=="Robb"):
	lobo= "Vento Cinzento"
elif(stark=="Rickon"):
	lobo="Cao Felpudo"
elif(stark=="Jon Snow"):
	lobo="Fantasma"
elif(stark=="Bran"):
	lobo="Verao"
elif(stark=="Arya"):
	lobo="Nymeria"
else:
	lobo="invalida"
if(stark=="Sansa")or(stark=="Robb")or(stark=="Rickon")or(stark=="Jon Snow")or(stark=="Bran")or(stark=="Arya"):
	print(lobo)
else:
	print("Entrada",stark,"invalida")