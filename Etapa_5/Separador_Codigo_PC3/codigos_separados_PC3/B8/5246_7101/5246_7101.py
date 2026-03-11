idade = int(input("Idade: "))
peso = float(input("Peso: "))
print("Entradas:",idade,"anos e",round(peso,1),"kg")
if (0<=idade<=130 and 0<=peso<=550):
	if (idade>50 and peso>90):
		print("Grupo de risco: 1")
	elif (idade>50 and 60<peso<=90):
		print("Grupo de risco: 2")
	elif (idade>50 and peso<=60):
		print("Grupo de risco: 3")
	elif (20<idade<=50 and peso>90):
		print("Grupo de risco: 4")
	elif (20<idade<=50 and 60<peso<=90):
		print("Grupo de risco: 5")
	elif (20<idade<=50 and peso<=60):
		print("Grupo de risco: 6")
	elif (idade<=20 and peso>90):
		print("Grupo de risco: 7")
	elif (idade<=20 and 60<peso<=90):
		print("Grupo de risco: 8")
	elif (idade<=20 and peso<=60):
		print("Grupo de risco: 9")
else:
	print("Dados invalidos")