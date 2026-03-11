idade = int(input("digite a idade do paciente"))
peso = float(input("digite o peso do paciente em Kg"))
round(peso, 2)
print("Entradas:", idade, "anos", "e", peso, "kg")

if (idade > 0) and (idade <= 130) and (peso >= 0) and (peso <= 550):
	if (peso >= 60) and (idade > 12):
		dosagem = 1000
		print("Dosagem:", dosagem, "mg")
	elif (peso < 60) and (idade > 12):
		dosagem = 875
		print("Dosagem:", dosagem, "mg")
	elif (peso <= 5) and (idade < 12):
		dosagem = 75
		print("Dosagem:", dosagem, "mg")
	elif (peso > 5) and (peso <= 9) and (idade < 12):
		dosagem = 125
		print("Dosagem:", dosagem, "mg")
	elif (peso > 9) and (peso <= 16) and (idade < 12):
		dosagem = 250
		print("Dosagem", dosagem, "mg")
	elif (peso > 16) and (peso <= 24) and (idade < 12):
		dosagem = 375
		print("Dosagem:", dosagem, "mg")
	elif (peso > 24) and (peso <= 30) and (idade < 12):
		dosagem = 500
		print("Dosagem:", dosagem, "mg")
	elif (peso > 30) and (idade < 12):
		dosagem = 750
		print("Dosagem:", dosagem, "mg")
else:
	print("Dados invalidos")
		