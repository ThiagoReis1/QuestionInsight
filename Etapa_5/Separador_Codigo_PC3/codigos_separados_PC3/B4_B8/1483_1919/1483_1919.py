nome = input("Qual o nome do equipamento: ").upper()
quant = int(input("Qual a quantidade a ser transportada: "))
if((quant<0) or (quant>1000) or nome != nome):
	print("Entrada invalida")
elif(nome == "COMPUTADOR"):
	print(round(quant * 12, 2))
elif(nome == "FREEZER"):
	print(round(quant * 52, 2))
elif(nome == "FURADEIRA"):
	print(round(quant * 1.7, 2))
elif(nome == "LIQUIDIFICADOR"):
	print(round(quant * 1.8, 2))
elif(nome == "MICROONDAS"):
	print(round(quant * 15, 2))
elif(nome == "NOTEBOOK"):
	print(round(quant * 2.5, 2))
elif(nome == "TELEVISOR"):
	print(round(quant * 15, 2))
elif(nome == "VENTILADOR"):
	print(round(quant * 2.4, 2))