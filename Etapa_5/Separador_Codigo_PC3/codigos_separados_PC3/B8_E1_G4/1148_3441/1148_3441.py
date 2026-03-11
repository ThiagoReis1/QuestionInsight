x= input("nome da regiao: ")
#regiao
if x=="Norte" or x=="Vale" or x=="Terras fluviais" or x=="Terras da tempestade" or x=="Dorne" or x=="Ilhas de ferro" or x=="Campina" or x=="Terras ocidentais" or x=="Terras da coroa":
	if x == "Norte":
		print("Snow")
	elif x == "Vale":
		print("Stone")
	elif x == "Terras fluviais":
		print("Rivers")
	elif x=='Terras da tempestade':
		print('Storm')
	elif x == 'Dorne':
		print("Sand")
	elif x == 'Ilhas de ferro':
		print('Pyke')
	elif x == "Campina":
		print('Flowers')
	elif x == "Terras ocidentais":
		print('Hill')
	elif x == "Terras da coroa":
		print("Waters")
else:
	print("Entrada", x, "invalida")