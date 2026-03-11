idade = int(input("diga sua idade"))
peso = float(input("informe seu peso"))
print("Entradas:", idade, "anos e", peso, "kg")

#definição dos grupos de risco
if(0 <= idade <= 130 and 0.0 <= peso <= 550.0):
	if(idade <= 20):
		if(peso <= 60):
			gr = 9
		elif(peso <= 90):
			gr = 8
		else:
			gr = 7
	elif(idade <= 50):
		if(peso <= 60):
			gr = 6
		elif(peso <= 90):
			gr = 5
		else:
			gr = 4
	elif(idade > 50):
		if(peso <= 60):
			gr = 3
		elif(peso <= 90):
			gr = 2
		else:
			gr = 1
else:
	gr = -1
#Resultados
if(gr == -1):
	print("Dados invalidos")
else:
	print("Grupo de risco:", gr)
			

		