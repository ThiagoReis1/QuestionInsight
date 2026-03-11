idade=int(input("Qual a idade: "))
peso=float(input("Qual o peso: "))

if(idade >= 0 and idade <= 130 and peso >= 0.0 and peso <= 550.0):
	if(idade <= 20):
		if(peso <= 60):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 9")
		elif(peso >= 60 or peso <= 90):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 8")
		else:
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 7")
	elif(idade >= 20 or idade <= 50):
		if(peso <= 60):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 6")
		elif(peso >= 60 or peso <= 90):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 5")
		else:
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 4")
	else:
		if(peso <= 60):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 3")
		elif(peso >= 60 or peso <= 90):
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 2")
		else:
			print("Entradas:", idade, "anos e", peso, "kg")
			print("Grupo de risco: 1")
else:
	print("Entradas:", idade, "anos e", peso, "kg")
	print("Dados invalidos")
	