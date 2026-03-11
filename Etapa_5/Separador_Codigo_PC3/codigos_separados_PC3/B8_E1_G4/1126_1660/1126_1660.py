nome = input("Qual o nome do Stark? ")

if (nome == "Sansa" or nome == "Robb" or nome == "Rickon" or nome == "Jon Snow" or   nome == "Bran" or nome == "Arya"):
	if (nome == "Sansa"):
		print("Lady")
	elif (nome == "Robb"):
		print("Vento Cinzento")
	elif (nome == "Rickon"):
		print("Cao Felpudo")
	elif (nome == "Jon Snow"):
		print("Fantasma")
	elif (nome == "Bran"):
		print("Verao")
	elif (nome == "Arya"):
		print("Nymeria")
else:
	print("Entrada", nome, "invalida")