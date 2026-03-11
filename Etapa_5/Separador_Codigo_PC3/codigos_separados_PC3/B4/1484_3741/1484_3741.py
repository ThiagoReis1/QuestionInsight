equipamento = input("Digite: ")

capacidade = int(input("Digite: "))

if (capacidade >= 0) and (equipamento == "COMPUTADOR"):
	print(5000 // 12, 2)
elif (capacidade >= 0 ) and (equipamento == "FREEZER"):
	print(5000 // 52, 2)
elif (capacidade >= 0) and (equipamento == "FURADEIRA"):
	print(5000 // 17, 2)
elif (capacidade >= 0) and (equipamento == "LIQUIDIFICADOR"):
	print(5000 // 18)
elif (capacidade >= 0) and (equipamento == "MICROONDAS"):
	print(5000 // 15, 2)
elif (capacidade >= 0) and (equipamento == "NOTEBOOK"):
	print(5000 // 25, 2)
elif (capacidade >= 0) and (equipamento == "TELEVISOR"):
	print(5000 // 15, 2)
elif (capacidade >= 0) and (equipamento == "VENTILADOR"):
	print(5000 // 24, 2)
elif (capacidade < 0) or (capacidade > 1000):
	print("Entrada invalida")
else:
	print("Entrada invalida")
