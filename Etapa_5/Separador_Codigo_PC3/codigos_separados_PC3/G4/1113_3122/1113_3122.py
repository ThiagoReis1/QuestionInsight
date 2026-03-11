idade = int(input("Idade: "))
peso = float(input("Peso: "))

print("Entradas:", idade, "anos e", peso, "kg")

if(idade > 0) and (idade <= 130):
	if (peso > 0 ) and (peso <= 550):
		if (idade <= 20):
			if (peso <= 60):
				g9 = "9"
				print("Grupo de risco:", g9)
			elif (peso >= 60) and (peso <= 90):
				g8 = "8"
				print("Grupo de risco:", g8)
			else:
				g7 = "7"
				print("Grupo de risco:", g7)
		elif (idade >= 20) and (idade <=50):
			if (peso <= 60):
				g6 = "6"
				print("Grupo de risco:", g6)
			elif (peso >= 60) and (peso <= 90):
				g5 = "5"
				print("Grupo de risco:", g5)
			else:
				g4 = "4"
				print("Grupo de risco:", g4)
		else:
			if (peso <= 60):
				g3 = "3"						 
				print("Grupo de risco:", g3)
			elif (peso >= 60) and (peso <= 90):
				g2 = "2"
				print("Grupo de risco:", g2)
			else:
				g1 = "1"
				print("Grupo de risco:", g1)
				
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")