idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print("Entradas:", idade," anos e", peso,"kg")
if ((idade >= 0 and idade <= 130) and (peso >= 0.0 and peso <= 550.0)):
	if (idade >= 12):
		if(peso >= 60):
			dose = "1000 mg"
		else:
			dose = "875 mg"
	else:
			if (peso <= 5):
				dose = "75 mg"
			elif (peso > 5 and peso <= 9):
				dose = "125 mg"
			elif (peso > 9 and peso <= 16):
				dose = "250 mg"
			elif (peso > 16 and peso <= 24):
				dose = "375 mg"
			elif (peso > 24 and peso <= 30):
				dose = "500 mg"
			else:
				dose = "750 mg"
else:
	dose = -1

if (dose == -1):
	print("Dados invalidos")
else:
	print("Dosagem:", dose)
		