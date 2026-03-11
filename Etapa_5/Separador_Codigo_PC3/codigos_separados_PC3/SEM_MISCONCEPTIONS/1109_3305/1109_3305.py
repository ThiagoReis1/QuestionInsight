idade = int(input("entre com a idade: "))
peso = float(input("entre com o peso: "))
print("Entradas:", idade, "anos e", peso, "kg")
if((idade >=0 ) and (idade <= 130) and (peso > 0.0) and (peso <= 550.0)):
	if((idade>=12) and (peso>=60.0)):
		volume = 1000
		print("Dosagem:", volume, "mg")
	elif((idade>=12) and (peso<=60.0)):
		
	elif((idade<12) and (peso<=5.0)):
		volume = 75
		print("Dosagem:", volume, "mg")
	elif((idade<12) and (peso>5.0) and (peso<=9.0)):
		volume = 125
		print("Dosagem:", volume, "mg")
	elif((idade<12) and (peso>9.0) and (peso<=16.0)):
		volume = 250
		print("Dosagem:", volume, "mg")
	elif((idade<12) and (peso>16.0) and (peso<=24.0)):
		volume = 375
		print("Dosagem:", volume, "mg")
	elif((idade<12) and (peso>24.0) and (peso<=30.0)):
		volume = 500
		print("Dosagem:", volume, "mg")
	elif((idade<12) and (peso>30.0)):
		volume = 750
		print("Dosagem: ", volume, "mg")
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")