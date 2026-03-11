x  = input("Informe o sobrenome: ")

if(x == "Snow"):
	regiao = "Norte"
elif(x == "Stone"):
	regiao = "Vale"
elif(x == "Rivers"):
	regiao = "Terras Fluviais"
elif(x == "Storm"):
	regiao = "Terras da Tempestade"	
elif(x == "Sand"):
	regiao = "Dorne"
elif(x == "Pyke"):
	regiao = "Ilhas de Ferro"
elif(x == "Flowers"):
	regiao = "Campina"
elif(x == "Hill"):
	regiao = "Terras Ocidentais"
elif(x == "Waters"):
	regiao = "Terra da Coroa"
else:
	regiao = ("Entrada" ,x, "invalida")
	
print(regiao)