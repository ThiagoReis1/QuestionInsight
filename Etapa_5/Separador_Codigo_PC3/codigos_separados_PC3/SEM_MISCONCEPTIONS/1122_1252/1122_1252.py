#Patrick Chessmam - 21200931

bastardo = input("Digite o nome do bastardo: ")

if (bastardo == "Snow") :
	regiao = "Norte"
elif (bastardo == "Stone") :
	regiao = "Vale"
elif (bastardo == "Rivers") :
	regiao = "Terras Fluviais"
elif (bastardo == "Storm")	:
	regiao = "Terras da Tempestade"
elif (bastardo == "Sand")	:
	regiao = "Dorne"
elif (bastardo == "Pyke")	:	
	regiao = "Ilhas de Ferro"
elif (bastardo == "Flowers")	:
	regiao = "Campina" 
elif (bastardo == "Hill")	:
	regiao = "Terras Ocidentais"
elif (bastardo == "Waters"):
	regiao = "Terras da Coroa"
else:
	print ("Entrada", bastardo ,"invalida")
print(regiao)	
	