prato = int(input("Qual o prato escolhido? "))
desert = int(input("Qual a sobremesa escolhida? "))
drink = int(input("Qual a bebida escolhida? "))

if ((prato >= 1 and prato <= 4) and (desert >= 1 and desert <= 4) and (drink >= 1 and drink <= 4)):
	if (prato == 1):
		cal_pr = 180
	elif (prato == 2):
		cal_pr = 230
	elif (prato == 3):
		cal_pr = 250
	elif (prato == 4):
		cal_pr = 350
	if (desert == 1):
		cal_de = 75
	elif (desert == 2):
		cal_de = 110
	elif (desert == 3):
		cal_de = 170
	elif (desert == 4):
		cal_de = 200
	if (drink == 1):
		cal_dr = 20
	elif (drink == 2):
		cal_dr = 70
	elif (drink == 3):
		cal_dr = 100
	elif (drink == 4):
		cal_dr = 65
	total = cal_pr + cal_de + cal_dr
	print("Entradas:", prato, ",", desert, ",", drink)
	print("Calorias: ", total, "cal")
else:
	print("Entradas:", prato, ",", desert, ",", drink)
	print("Dados invalidos")	