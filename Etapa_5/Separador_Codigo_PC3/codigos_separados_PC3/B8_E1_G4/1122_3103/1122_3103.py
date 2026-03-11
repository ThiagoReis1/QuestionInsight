x = input("Qual o sobrenome do bastardo?: ")
if(x == "Snow" or x == "Stone" or x == "Rivers" or x =="Storm" or x == "Sand" or x == "Pyke" or x == "Flowers" or x == "Hill" or x == "Waters"):
	if(x == "Snow"):
		print("Norte")
	elif(x == "Stone"):
		print("Vale")
	elif(x == "Rivers"):
		print("Terras Fluviais")
	elif( x =="Storm"):
		print("Terras da Tempestade")
	elif(x == "Sand"):
		print("Dorne")
	elif( x == "Pyke"):
		print("Ilhas de Ferro")
	elif(x == "Flowers"):
		print("Campina")
	elif(x == "Hill"):
		print("Terras Ocidentais")
	elif(x == "Waters"):
		print("Terras da Coroa")
else:
	print("Entrada", x , "invalida")