nm = input("Digite o nome do Stark: ")
n = nm.upper()

if (n == "SANSA" or n == "ROBB" or n == "RICKON" or n == "JON SNOW" or n == "BRAN" or n == "ARYA"):
	if (n == "SANSA"):
		print("Lady")
	elif (n == "ROBB"):
		print("Vento Cinzento")
	elif (n == "RICKON"):
		print("Cao Felpudo")
	elif (n == "JON SNOW"):
		print("Fantasma")
	elif (n == "BRAN"):
		print("Verao")
	elif (n == "ARYA"):
		print("Nymeria")
	else:
		print("Entrada", nm, "invalida")
else:
	print("Entrada", nm, "invalida")