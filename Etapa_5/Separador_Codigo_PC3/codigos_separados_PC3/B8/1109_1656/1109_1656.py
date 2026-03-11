idade = int(input("a idade"))
peso = float(input("o peso"))
print("Entradas:" , idade , "anos e" , peso , "kg")
if (0 <= idade <= 130) and (0.0 <= peso <= 550.0):
	if (peso >= 60.0 and peso >= 0.0):
		print("Dosagem: 1000 mg")
	elif (peso < 60.0 and peso >= 0.0):
		print("Dosagem: 875 mg")
	elif (peso <= 5.0 and peso >= 0.0):
		print("Dosagem: 75 mg")
	elif (5.0 < peso <= 9.0):
		print("Dosagem: 125 mg")
	elif (9.0 < peso <= 16.0):
		print("Dosagem: 250 mg")
	elif (16.0 < peso <= 24.0):
		print("Dosagem: 375 mg")
	elif (24.0 < peso <= 30.0):
		print("Dosagem: 500 mg")
	elif (peso > 30.0 and peso >= 550.0):
		print("Dosagem: 750 mg")
else:
	print("Dados invalidos")
	