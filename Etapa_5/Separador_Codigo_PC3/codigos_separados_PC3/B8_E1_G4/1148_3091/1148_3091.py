nome = input("digite nome: ")

if((nome=="Norte")or(nome=="Vale")or(nome=="Terras Fluviais")or(nome=="Terras da Tempestade")or(nome=="Dorne")or(nome=="Ilhas de Ferro")or(nome=="Campina")or(nome=="Terras Ocidentais")or(nome=="Terras da Coroa")):
	if(nome=="Norte"):
		b = "Snow"

	elif(nome=="Vale"):
		b = "Stone"
	
	elif(nome=="Terras Fluviais"):
		b = "Rivers"

	elif(nome=="Terras da Tempestade"):
		b = "Storm"

	elif(nome=="Dorne"):
		b = "Sand"
	
	elif(nome=="Ilhas de Ferro"):
		b = "Pyke"

	elif(nome=="Campina"):
		b = "Flowers"
	
	elif(nome=="Terras Ocidentais"):
		b = "Hill"
	
	elif(nome=="Terras da Coroa"):
		b = "Waters"
	print(b)
else:
	print("Entrada", nome, "invalida")

