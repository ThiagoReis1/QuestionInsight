#Equipamentos e capacidade
n = input("Informe o nome do equipamento: ")
capacidade = int(input("Informe a capacidade de carga em quilos: "))

if (capacidade >= 0 and capacidade <=1000):
	if (n == "COMPUTADOR"):
		quantidade = capacidade//12 
	elif (n == "FREEZER"):
		quantidade = capacidade//52
	elif (n == "FURADEIRA"):
		quantidade = capacidade//1.7
	elif (n == "LIQUIDIFICADOR"):
		quantidade = capacidade//1.8
	elif (n == "MICROONDAS"):
		quantidade = capacidade//15
	elif (n == "NOTEBOOK"):
		quantidade = capacidade//2.5
	elif (n == "TELEVISOR"):
		quantidade = capacidade//15
	elif (n == "VENTILADOR"):
		quantidade = capacidade//2.4
	print(quantidade)
else:
	print("Entrada invalida")

		
		
		

