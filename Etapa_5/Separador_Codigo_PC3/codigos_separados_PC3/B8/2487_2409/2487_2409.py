prato = int(input("digite o prato: "))
sobremesa = int(input("digite a sobremesa: "))
bebida = int(input("digite a bebida: "))

print("Entradas:", prato, ",", sobremesa, ",", bebida)

total_caloria = 0
if((prato != 1 and prato != 2 and prato != 3 and prato != 4) and (sobremesa != 1 and sobremesa != 2 and sobremesa != 3 and sobremesa != 4 and (bebida != 1 and bebida != 2 and bebida != 3 and bebida != 4))):
	print("Dados invalidos")
if(not(prato != 1 and prato != 2 and prato != 3 and prato != 4)):
	if(prato == 1):
		caloria = 180
		total_caloria = total_caloria + caloria
	elif(prato == 2):
		caloria = 230
		total_caloria = total_caloria + caloria
	elif(prato == 3):
		caloria = 250
		total_caloria = total_caloria + caloria
	elif(prato == 4):
		caloria = 350
		total_caloria = total_caloria + caloria
if(not(sobremesa != 1 and sobremesa != 2 and sobremesa != 3 and sobremesa != 4)):
	if(sobremesa == 1):
		caloria = 75
		total_caloria = total_caloria + caloria
	elif(sobremesa == 2):
		caloria = 110
		total_caloria = total_caloria + caloria
	elif(sobremesa == 3):
		caloria = 170
		total_caloria = total_caloria + caloria
	elif(sobremesa == 4):
		caloria = 200
		total_caloria = total_caloria + caloria
if(not(bebida != 1 and bebida != 2 and bebida != 3 and bebida != 4)):
	if(bebida == 1):
		caloria = 20
		total_caloria = total_caloria + caloria
	elif(bebida == 2):
		caloria = 70
		total_caloria = total_caloria + caloria
	elif(bebida == 3):
		caloria = 100
		total_caloria = total_caloria + caloria
	elif(bebida == 4):
		caloria = 65
		total_caloria = total_caloria + caloria
print("Calorias:", total_caloria, "cal")
