a = input("Digite: ")

if(a == "Snow" or a == "Stone" or a=="Rivers" or a=="Storm" or a=="Sand" or a== "Pyke" or a=="Flowers" or a== "Hill" or a=="Waters"):
	if(a == "Snow"):
		print("Norte")
	elif(a=="Stone"):
		print("Vale")
	elif(a=="Rivers"):
		print("Terras Fluviais")
	elif(a== "Storm"):
		print("Terras da Tempestade")
	elif(a=="Sand"):
		print("Dorne")
	elif(a=="Pyke"):
		print("Ilhas de Ferro")
	elif(a=="Flowers"):
		print("Campina")
	elif("Hill"):
		print("Terras Ocidentais")
	elif("Waters"):
		print("Terras da Coroa")
else:
	print("Entrada",a,"invalida")
