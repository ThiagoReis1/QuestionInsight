regiao = input("Informe o nome da região: ")

if(regiao == "Norte"):
	bastardo = "Snow"
elif(regiao == "Vale"):
	bastardo = "Stone"	
elif(regiao == "Terras Fluviais"):
	bastardo = "Rivers"
elif(regiao == "Terras da Tempestade"):
	bastardo = "Storm"
elif(regiao == "Dorne"):
	bastardo = "Sand"
elif(regiao == "Ilhas de Ferro"):
	bastardo = "Pyke"
elif(regiao == "Campina"):
	bastardo = "Flowers"
elif(regiao == "Terras Ocidentais"):
	bastardo = "Hill"
elif(regiao == "Terras da Coroa"):
	bastardo = "Waters"
else: 
	bastardo = "Entrada X invalida"
print(bastardo)	