idade=int(input("idade: "))
peso=float(input("peso: "))

if (idade >= 0) and (idade <= 20):
	if (peso >= 0.0) and (peso <= 60.0):
		g= 9
		print("Entradas:",idade, "anos", "e",round(peso, 1),"kg")
		print("Grupo de risco:", g)
	else:
		if (peso > 60.0) and (peso <= 90.0):
			g1= 8
			print("Entradas:",idade, "anos", "e",round(peso, 1),"kg")
			print("Grupo de risco:", g1)
		else:
			if (peso > 90.0):
				g2= 7
				print("Entradas:",idade, "anos", "e",round(peso, 1),"kg")
				print("Grupo de risco:", g2)
			elif (peso < 0.0) or (peso > 550.0):
				print("Dados invalidos")
elif (idade > 20) and (idade <= 50):
	if (peso >= 0.0) and (peso <= 60.0):
		g3= 6
		print("Entradas:",idade, "anos", "e",round(peso, 1),"kg")
		print("Grupo de risco:", g3)
	else:
		if (peso > 60.0) and (peso <= 90.0):
			g4= 5
			print("Entradas:",idade, "anos", "e",round(peso, 1),"kg")
			print("Grupo de risco:", g4)
		else:
			if (peso > 90.0):
				g5= 4
				print("Entradas:", idade, "anos", "e",round(peso, 1),"kg")
				print("Grupo de risco:", g5)
			elif (peso < 0.0) or (peso > 550.0):
				print("Dados invalidos")
elif (idade > 50):
	if (peso >= 0.0) and (peso <= 60.0):
		g6= 3
		print("Entradas:", idade, "anos", "e",round(peso, 1),"kg")
		print("Grupo de risco:", g6)
	else:
		if (peso > 60.0) and (peso <= 90.0):
			g7= 2
			print("Entradas:", idade, "anos", "e",round(peso, 1),"kg")
			print("Grupo de risco:", g7)
		else:
			if (peso > 90.0):
				g8= 1
				print("Entradas:", idade, "anos", "e",round(peso, 1),"kg")
				print("Grupo de risco:", g8)
			else:
				print("Entradas:", idade, "anos", "e",round(peso, 1),"kg")
				print("Dados invalidos")
else:
	print("Entradas", idade, "anos", "e", round(peso, 1),"kg")
	print("Dados invalidos")
				

