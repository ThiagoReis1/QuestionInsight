Casa = str(input("qual o nome da Casa:"))

if(Casa == "Baratheon"):
	regiao = "Ponta da Tempestade"
elif(Casa == "Targaryen"):
	regiao = "Ilha do Dragao"
elif(Casa == "Tyrell"):
	regiao = "Campina"
elif(Casa == "Stark"):
	regiao = "Winterfell"
elif(Casa == "Lannister"):
	regiao = "Rochedo Casterly"
elif(Casa == "Geyjoy"):
	regiao = "Pyke"
elif(Casa == "Tully"):
	regiao = "Correrio"
elif(Casa == "Arryn"):
	regiao = "Ninho da Aguia"
elif(Casa == "Martell"):
	regiao = "Dorne"
else: 
	regiao = "Entrada invalida"
	
print(regiao)