idade = int(input("Idade:"))
peso = float(input("Peso:"))
print ("Entradas:",idade,"anos e",peso,"kg")
if ((0 <= idade <= 130) and (0 <= peso <= 550 )):
	if (idade >= 12): #adultos e adolescentes
		if(peso >= 50):
			dosagem = 1000
		else:
			dosagem = 875
	else:
		if (peso <= 5):
			dosagem = 75
		elif (peso <= 9):
			dosagem = 125
		elif (peso <= 16):
			dosagem = 250
		elif (peso <= 24):
			dosagem = 375
		elif (peso <= 30):
			dosagem = 500
		else:
			dosagem = 750
	print("Dosagem:", dosagem,"mg")
else:
	print("Dados invalidos")