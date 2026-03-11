x = input("Insira a cidade livre: ")
if ( x == "Pentos" or x == "Bravos" or x == "Lys" or x == "Qohor" or x == "Norvos" or x == "Myr" or x == "Tyrosh" or x == "Volantis" or x == "Lorath"):
	if (x == "Pentos"):
		print("pentoshi")
	elif ( x == "Bravos"):
		print("bravosiano")
	elif ( x == "Lys"):
		print("liseno")
	elif (x == "Qohor"):
		print("qohorik")
	elif (x == "Norvos"):
		print("norvoshi")
	elif (x == "Myr"):
		print("myrano")
	elif (x == "Tyrosh"):
		print("tyroshi")
	elif (x == "Volantis"):
		print("volantino")
	else:
		print("lorathi")
else:
	print("Entrada", x, "invalida")