regiao= (input())

if(regiao == "Norte") or (regiao == "Vale") or (regiao=="Terras Fluviais") or (regiao=="Terras da Tempestade") or (regiao == "Dorne") or (regiao=="Ilhas de Ferro") or (regiao=="Campina") or (regiao=="Terras Ocidentais") or (regiao=="Terras da Coroa"):
	if(regiao=="Norte"):
		print("Snow")
	elif(regiao == "Vale"):
		print("Stone")
	elif(regiao=="Terras Fluviais"):
		print("Rivers")
	elif(regiao=="Terras da Tempestade"):
		print("Storm")
	elif(regiao == "Dorne"):
		print("Sand")
	elif(regiao=="Ilhas de Ferro"):
		print("Pyke")
	elif(regiao=="Campina"):
		print("Flowers")
	elif(regiao=="Terras Ocidentais"):
		print("Hill")
	elif(regiao=="Terras da Coroa"):
		print("Waters")
else:
	print("Entrada",regiao,"invalida")