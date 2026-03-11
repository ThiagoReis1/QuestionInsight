idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
PESO = round(peso, 1)

print("Entradas:", idade, "anos e",PESO, "kg")

if ((idade > 0) and (idade <= 20)):
	if (peso > 0) and (peso <= 60):
		print("Grupo de risco: 9")
	elif (peso > 60) and (peso <= 90):
		print("Grupo de risco: 8")
	elif (peso > 90):
		print("Grupo de risco: 7")
	else:
		print("Dados invalidos")
elif ((idade > 20) and (idade <= 50)):
	if (peso > 0) and (peso <= 60):
		print("Grupo de risco: 6")
	elif (peso > 60) and (peso <= 90):
		print("Grupo de risco: 5")
	elif (peso > 90):
		print("Grupo de risco: 4")
	else:
		print("Dados invalidos")
elif (idade >50):
	if (peso > 0) and (peso <= 60):
		print("Grupo de risco: 3")
	elif (peso > 60) and (peso <= 90):
		print("Grupo de risco: 2")
	elif (peso > 90):
		print("Grupo de risco: 1")
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")