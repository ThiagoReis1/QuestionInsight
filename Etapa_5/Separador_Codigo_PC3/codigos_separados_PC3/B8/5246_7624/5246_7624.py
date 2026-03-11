idade = int(input("digite a idade: "))
peso = float(input("digite o peso: "))

if ((idade > 0) and (idade < 130) and (peso > 0.0) and (peso < 550.0)):
	if ((idade <= 20) and (peso <= 60)):
		print("Grupo de risco: 9")
	elif ((idade <= 20) and ((peso > 60) and (peso <= 90))):
		print("Grupo de risco: 8")
	elif ((idade <= 20) and (peso > 90)):
		print("Grupo de risco: 7")
	elif (((idade > 20) and (idade <= 50)) and (peso <= 60)):
		print("Grupo de risco: 6")
	elif (((idade > 20) and (idade <= 50)) and ((peso > 60) and (peso <= 90))):
		print("Grupo de risco: 5")
	elif (((idade > 20) and (idade <= 50)) and (peso > 90)):
		print("Grupo de risco: 4")
	elif ((idade > 50) and (peso <= 60)):
		print("Grupo de risco: 3")
	elif ((idade > 50) and ((peso > 60) and (peso <= 90))):
		print("Grupo de risco: 2")
	elif ((idade > 50) and (peso > 90)):
		print("Grupo de risco: 1")
else:
	print("Dados invalidos")