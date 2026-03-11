x = input()

if (x.lower() != "norte") and (x.lower() != "vale") and (x.lower() != "terras fluviais") and (x.lower() != "terras da tempestade") and (x.lower() != "dorne") and (x.lower() != "ilhas de ferro") and (x.lower() != "campina") and (x.lower() != "terras ocidentais") and (x.lower() != "terras da coroa"):
	print("Entrada", x, "invalida")
elif(x.lower()== "Norte"):
	print("snow")
elif(x.lower() == "Vale"):
	print("stone")
elif(x.lower() == "Terras Fluviais"):
	print("rivers")
elif(x.lower() == "Terras da Tempestade"):
	print("storm")
elif(x.lower() == "Dorne"):
	print("sand")
elif(x.lower() == "Ilhas de Ferro"):
	print("pyke")
elif(x.lower() == "Campina"):
	print("flowers")
elif(x.lower() == "Terras Ocidentais"):
	print("hill")
else:
	print("waters")
