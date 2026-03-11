nome = str(input("Qual o nome do bastardo?"))

if(nome == "Snow"):
	regiao = "Norte"
elif(nome == "Stone"):
	regiao == "Vale"
elif(nome == "Rivers"):
	regiao = "Terras Fluviais"
elif(nome == "Storm"):
	regiao = "Terras da Tempestade"
elif(nome == "Sand"):
	regiao = "Dorne"
elif(nome == "Pyke"):
	regiao = "Ilhas de Ferro"
elif(nome == "Flowers"):
	regiao = "Campina"
elif(nome == "Hill"):
	regiao = "Terras Ocidentais"
elif(nome == "Waters"):
	regiao = "Terras da Coroa"
else:
	regiao = "invalida"


if(regiao == "invalida"):
	print("Entrada", regiao, "invalida")
else:
	print(regiao)

	