idade = int(input("qual sua idade:"))
peso = float(input("qual sua massa corporal:"))

if (idade > 0) and (peso > 0):
	if (idade <= 20):
		if (peso <= 60):
			print("Grupo de risco: 9")
		elif (peso > 60) and (peso <= 90):
			print("Grupo de risco: 8")
		elif (peso > 90):
			print("Grupo de risco 7")
	if (idade > 20) and (idade <= 50):
		if (peso <= 60):
			print("Grupo de risco: 6")
		elif (peso > 60) and (peso <= 90):
			print("Grupo de risco: 5")
		elif (peso > 90):
			print("grupo de risco: 4")
	if (idade > 50):
		if (peso <= 60):
			print("Grupo de risco: 3")
		elif (peso > 60) and (peso <= 90):
			print("Grupo de risco: 2")
		elif (peso >90):
			print("Grupo de risco: 1")
else:
	print("Dados invalidos")