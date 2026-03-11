casa = input("Insira o nome da casa: ")
if(casa == "Baratheon" or casa == "Targaryen" or casa == "Tyrell" or casa == "Stark" or casa == "Lannister" or casa == "Grejoy" or casa == "Tully" or casa == "Arryn" or casa == "Martell"):
	if(casa == "Baratheon"):
		print("Ponta Tempestade")
	elif(casa == "Targaryen"):
		print("Ilha do Dragao")
	if(casa == "Tyrell"):
		print("Campina")
	elif(casa == "Stark"):
		print("Winterfell")
	if(casa == "Lannister"):
		print("Rochedo Casterly")
	elif(casa == "Grejoy"):
		print("Pyke")
	if(casa == "Tully"):
		print("Correrio")
	elif(casa == "Arryn"):
		print("Ninho de Aguia")
	if(casa == "Martell"):
		print("Dorne")
else:
	print("Entrada ", casa, "invalida")