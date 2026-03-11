casa = str(input("Informe a casa: "))

if(casa == "Baratheon" or casa == "Targaryen" or casa == "Tyrell" or casa == "Stark" or  casa == "Lannister" or casa == "Greyjoy" or casa == "Tully" or casa == "Arryn" or casa == "Martell"):
	if(casa == "Baratheon"):
		lema = "Nossa eh a furia"
	elif(casa == "Targaryen"):
		lema = "Fogo e sangue"
	elif(casa == "Tyrell"):
		lema = "Crescendo fortes"
	elif(casa == "Stark"):
		lema = "O inverno esta chegando"
	elif(casa == "Lannister"):
		lema = "Oucam-me rugir"
	elif(casa == "Greyjoy"):
		lema = "Nos nao semeamos"
	elif(casa == "Tully"):
		lema = "Familia, dever, honra"
	elif(casa == "Arryn"):
		lema = "Tao alto como a honra"
	elif(casa == "Martell"):
		lema = "Insubmissos, nao curvados, nao quebrados"
else:
	lema = -1
	
if(lema == -1):
	print("Entrada", casa, "invalida")
else:
	print(lema)
	