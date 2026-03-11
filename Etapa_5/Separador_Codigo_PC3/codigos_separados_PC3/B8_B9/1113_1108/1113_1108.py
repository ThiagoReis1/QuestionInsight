idade = int(input())
peso = float(input())
cond1 = (idade >= 0 and idade < 130)
cond2 = (peso > 0.0 and peso < 550.0)

if (cond1 and cond2):
	if (idade <= 20):
		if (peso <= 60):
			grupo = "9"
		elif (peso > 60 and peso <= 90):
			grupo = "8"
		elif (peso > 90):
			grupo = "7"
	elif (idade > 20 and idade <= 50):
		if (peso <= 60):
			grupo = "6"
		elif (peso > 60 and peso <= 90):
			grupo = "5"
		elif (peso > 90):
			grupo = "4"
	else:
		if (peso <= 60):
			grupo = "3"
		elif (peso > 60 and peso <= 90):
			grupo = "2"
		elif (peso > 90):
			grupo = "1"
	print("Entradas:", idade, "anos e", peso ,"kg")
	print("Grupo de risco:", grupo)
	
else:
	print("Entradas:", idade, "anos e", peso ,"kg")
	print("Dados invalidos")
	

	