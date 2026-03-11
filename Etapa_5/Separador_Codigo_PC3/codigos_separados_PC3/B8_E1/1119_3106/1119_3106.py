casa_dos_tronos = input("Digite o nome da casa: ")

casa = casa_dos_tronos.lower()

if ((casa == "baratheon") or (casa == "targaryen") or (casa == "tyrell") or (casa == "stark") or (casa == "lannister") or (casa == "greyjoy") or (casa == "tully") or (casa == "arryn") or (casa == "martell")) :
	
	if(casa == "baratheon"):
		print("Nossa e a fúria")
	
	elif(casa == "targaryen"):
		print("Fogo e sangue")
		
	elif(casa == "tyrell"):
		print("Crescendo fortes")
		
	elif(casa == "stark"):
		print("O inverno esta chegando")
		
	elif(casa == "lannister"):
		print("Oucam-me rugir")
	
	elif(casa == "greyjoy"):
		print("Nos nao semeamos")
		
	elif(casa == "tully"):
		print("Familia, dever, honra")
		
	elif(casa == "arryn"):
		print("Tao alto como a honra")
		
	elif(casa == "martell"):
		print("Insubmissos, nao curvados, nao quebrados")
		
else:
	print("Entrada", casa_dos_tronos ,"invalida")
		