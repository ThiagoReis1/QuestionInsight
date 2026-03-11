reg = input("Qual a sua regiao? ")

if(reg=="Norte" or reg=="Vale" or reg=="Terras Fluviais" or reg=="Terras da Tempestade" or reg=="Dorne" or reg=="Ilhas de Ferro" or reg== "Campina" or reg=="Terras Ocidentais" or reg=="Terras da Coroa"):
	if(reg=="Norte"):
		print("Snow")
	elif(reg=="Vale"):
		print("Stone")
	elif(reg=="Terras Fluviais"):
		print("Rivers")
	elif(reg=="Terras da Tempestade"):
		print("Storm")
	elif(reg=="Dorne"):
		print("Sand")
	elif(reg=="Ilhas de Ferro"):
		print("Pyke")
	elif(reg=="Campina"):
		print("Flowers")
	elif(reg=="Teras Ocidentais"):
		print("Hill")
	else:
		print("Waters")
else:
	print("Entrada",reg,"invalida")