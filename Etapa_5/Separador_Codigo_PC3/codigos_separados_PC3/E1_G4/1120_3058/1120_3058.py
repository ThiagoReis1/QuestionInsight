casa= input("Qual o nome da casa?")

if(casa == "Baratheon") or (casa == "Targaryen") or (casa == "Tyrell") or (casa == "Stark") or (casa == "Lannister") or (casa == "Greyjoy") or (casa == "Tully") or (casa == "Arryn") or (casa == "Martell"):
	if(casa == "Baratheon"):
		print("Ponta Tempestade")
	if(casa == "Targaryen"):
		print("Ilha do Dragao")
	if(casa == "Tyrell"):
		print("Campina")
	if(casa == "Stark"):
		print("Winterfell")
	if(casa == "Lannister"):
		print("Rochedo Casterly")
	if(casa == "Greyjoy"):
		print("Pyke")
	if(casa == "Tully"):
		print("Correrio")
	if(casa == "Arryn"):
		print("Ninho da Aguia")
	if(casa == "Martell"):
		print("Dorne")
else:
	print("Entrada", casa, "invalida")
	