nome = input("Qual o sobrenome do bastardo: ")

if( nome == "Snow" or nome == "Stone" or nome == "Rivers" or nome == "Storm" or nome == "Sand" or nome == "Pyke" or nome == "Flowers" or nome == "Hill" or nome == "Waters"):
	if (nome == "Snow"):
		print ("Norte")
	elif (nome == "Stone"):
		print ("Vale")
	elif (nome == "Rivers"):
		print ("Terras Fluviais ")
	elif (nome == "Storm"):
		print ("Terras da Tempestade")
	elif (nome == "Sand"):
		print ("Dorne")
	elif (nome == "Pyke"):
		print ("Ilhas de Ferro")
	elif (nome == "Flowers"):
		print ("Campina")
	elif (nome == "Hill"):
		print ("Terras Ocidentais")
	elif (nome == "Waters"):
		print ("Terras da Coroa")
else:
   print("Entrada", nome, "invalida")
	