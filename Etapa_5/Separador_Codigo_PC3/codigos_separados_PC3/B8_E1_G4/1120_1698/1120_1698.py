casa = input("Diga a casa:")

if (casa == "Baratheon" or casa == "Targaryen" or casa == "Tyrell" or casa == "Stark" or casa == "Lannister" or casa == "Greyjoy" or casa == "Tully" or casa == "Arryn" or casa == "Martell"):
	if (casa == "Baratheon"):
		print("Ponta Tempestade")
	elif (casa == "Targaryen"):
		print("Ilha do Dragão")
	elif (casa == "Tyrell"):
		print("Campina")
	elif (casa == "Stark"):
		print("Winterfell")
	elif (casa == "Lannister"):
		print("Rochedo Casterly")
	elif (casa == "Greyjoy"):
		print("Pyke")
	elif (casa == "Tully"):
		print("Correrio")
	elif (casa == "Arryn"):
		print("Ninho da Aguia")
	elif (casa == "Martell"):
		print("Dorne")
else:
	print("Entrada", casa,"invalida")