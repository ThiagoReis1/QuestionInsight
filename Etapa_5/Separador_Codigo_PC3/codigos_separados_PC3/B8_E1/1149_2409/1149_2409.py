regiao = input("digite a regiao: ")

if(regiao != "Ponta Tempestade" and regiao != "Ilha do Dragao" and regiao != "Campina" and regiao != "Winterfell" and regiao != "Rochedo Casterly" and regiao != "Pyke" and regiao != "Correrio" and regiao != "Ninho da Aguia" and regiao != "Dorne"):
	print("Entrada", regiao, "invalida")
else:
	if(regiao == "Ponta Tempestade"):
		casa = "Baratheon"
	elif(regiao == "Ilha do Dragao"):
		casa = "Targaryen"
	elif(regiao == "Campina"):
		casa = "Tyrell"
	elif(regiao == "Winterfell"):
		casa = "Stark"
	elif(regiao == "Rochedo Casterly"):
		casa = "Lannister"
	elif(regiao == "Pyke"):
		casa = "Greyjoy"
	elif(regiao == "Correrio"):
		casa = "Tully"
	elif(regiao == "Ninho da Águia"):
		casa = "Arryn"
	elif(regiao == "dorne"):
		casa = "Martell"
	print(casa)