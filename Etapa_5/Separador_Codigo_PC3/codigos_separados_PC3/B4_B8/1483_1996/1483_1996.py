#Ex 01

equipamento = input("Qual o nome do equipamento? ") .upper()
quantidade = int(input("Quantos equipamentos serão transportados? "))

if ((quantidade >= 0) and (quantidade <= 1000)):
	if (equipamento == "COMPUTADOR"):
		conta = (quantidade * 12)
		print(round(conta,2))
	elif (equipamento == "FREEZER"):
		conta = (quantidade * 52)
		print(round(conta,2))
	elif (equipamento == "FURADEIRA"):
		conta = (quantidade * 1.7)
		print(round(conta,2))
	elif (equipamento == "LIQUIDIFICADOR"):
		conta = (quantidade * 1.8)
		print(round(conta,2))
	elif (equipamento == "MICROONDAS"):
		conta = (quantidade * 15)
		print(round(conta,2))
	elif (equipamento == "NOTEBOOK"):
		conta = (quantidade * 2.5)
		print(round(conta,2))
	elif (equipamento == "TELEVISOR"):
		conta = (quantidade * 15)
		print(round(conta,2))
	elif (equipamento == "VENTILADOR"):
		conta = (quantidade * 2.4)
		print(round(conta,2))
		
else:
	print("Entrada invalida")