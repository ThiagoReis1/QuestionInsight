idade= int(input("Insira a idade "))
peso= float(input("Insira o peso "))
if (idade >=0 and idade <=130) and (peso >=0,0 and peso <=550,0):
	if (idade >= 12) and (peso >= 60):
		dosagem= 1000
	elif (idade >= 12) and (peso < 60):
		dosagem= 875
	elif (idade < 12) and (peso <= 5):
		dosagem= 75
	elif (idade < 12) and (peso > 5 and peso <= 9):
		dosagem= 125
	elif (idade < 12) and (peso > 9 and peso <= 16):
		dosagem= 250
	elif (idade < 12) and (peso > 16 and peso <= 24):
		dosagem= 375
	elif (idade < 12) and (peso > 24 and peso <= 30):
		dosagem= 500
	elif (idade < 12) and (peso > 30):
		dosagem= 750
		print("Entradas:",idade, "anos e",peso,"kg")
		print("Dosagem:",dosagem,"mg")
else:
	print("Entradas:",idade, "anos e",peso,"kg")
	print("Dados invalidos")