
ent=input("Nome do equipamento:").upper()
qtd=int(input("Quantidade a ser transportada:"))

if(qtd < 0 or qtd > 1000):
	print("Entrada invalida")
elif(ent == "COMPUTADOR" or ent == "FREEZER" or ent == "FURADEIRA" or ent == "LIQUIDIFICADOR" or ent == "MICROONDAS" or ent == "NOTEBOOK" or ent == "TELEVISOR" or ent == "VENTILADOR"):
	if(ent == "COMPUTADOR"):
		peso=12
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "FREEZER"):
		peso=52
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "FURADEIRA"):
		peso=1.7
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "LIQUIDIFICADOR"):
		peso=1.8
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "MICROONDAS"):
		peso=15
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "NOTEBOOK"):
		peso=2.5
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "TELEVISOR"):
		peso=15
		pesototal=peso * qtd
		print(round(pesototal, 2))
	elif(ent == "VENTILADOR"):
		peso=2.4
		pesototal=peso * qtd
		print(round(pesototal, 2))
elif(ent != "COMPUTADOR" and ent != "FREEZER" and ent != "FURADEIRA" and ent != "LIQUIDIFICADOR" and ent != "MICROONDAS" and ent != "NOTEBOOK" and ent != "TELEVISOR" and ent != "VENTILADOR"):
	print("Entrada invalida")
