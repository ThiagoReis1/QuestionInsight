idade = int(input("Idade: "))
peso = float(input("Peso: "))
print("Entradas:",idade, "anos e", peso, "kg")
if(idade > 0 and idade < 130 and peso > 0.0 and peso < 550.0):
	if(idade <= 20 and peso <= 60):
		z = "9"
		print("Grupo de risco:", z)
	elif(idade <= 20 and (peso > 60 and peso <= 90)):
		z = "8"
		print("Grupo de risco:", z)
	elif(idade <= 20 and peso > 90):
		z = "7"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and peso < 60):
		z = "6"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and (peso > 60 and peso <= 90)):
		z = "5"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and peso > 90):
		z = "4"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso < 60):
		z = "3"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso > 60 and peso <= 90):
		z = "2"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso > 90):
		z = "1"
		print("Grupo de risco:", z)
else:
	print("Dados invalidos")