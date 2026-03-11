#--------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRICULA: 21456290
# DATA: 14/07/2016
#--------------------------------------------------------------

prato = int(input("Digite o numero correspondente ao prato: "))
sobremesa = int(input("Digite o numero correspondente a sobremesa: "))
bebida = int(input("Digite o numero correspondente a bebida: "))

print ("Entradas: ", prato, ", ", sobremesa, ", ", bebida)

if (prato <= 0 or prato > 4 and sobremesa <= 0 or sobremesa > 4 and bebida <= 0 or bebida > 4):
	print ("Dados invalidos")
else:
	if (prato == 1):
		cal1 = 180
	elif (prato == 2):
		cal1 = 230
	elif (prato == 3):
		cal1 = 250
	else:
		cal1 = 350
	if (sobremesa == 1):
		cal2 = 75
	elif (sobremesa == 2):
		cal2 = 110
	elif (sobremesa == 3):
		cal2 = 170
	else:
		cal2 = 200
	if (bebida == 1):
		cal3 = 20
	elif (bebida == 2):
		cal3 = 70
	elif (bebida == 3):
		cal3 = 100
	else:
		cal3 = 65
	soma = cal1 + cal2 + cal3
	print("Calorias: ", soma, "cal")
	