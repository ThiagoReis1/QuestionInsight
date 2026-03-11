nome = input("digite o nome do equipamento: ")
quantidade = int(input("digite a quantidade do equipamento: "))
if((quantidade>=0)and(quantidade<=1000)):
	if(nome=="COMPUTADOR"):
		print(round(12*quantidade, 2))
	elif(nome=="FREEZER"):
		print(round(52*quantidade, 2))
	elif(nome=="FURADEIRA"):
		print(round(1.7*quantidade, 2))
	elif(nome=="LIQUIDIFICADOR"):
		print(round(1.8*quantidade, 2))
	elif(nome=="MICROONDAS"):
		print(round(15*quantidade, 2))
	elif(nome=="NOTEBOOK"):
		print(round(2.5*quantidade, 2))
	elif(nome=="TELEVISOR"):
		print(round(15*quantidade, 2))
	elif(nome=="VENTILADOR"):
		print(round(2.4*quantidade, 2))
else:
	print("Entrada invalida")