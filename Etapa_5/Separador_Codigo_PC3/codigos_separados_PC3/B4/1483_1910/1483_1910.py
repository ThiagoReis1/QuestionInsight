nome = input("")
peso = int(input(""))
if(peso<0 or peso>1000):
	print("Entrada invalida")
else:
	if(nome == "COMPUTADOR"):
		quantidade = peso*12
	elif(nome == "FREEZER"):
		quantidade = peso*52
	elif(nome == "FURADEIRA"):
		quantidade = peso*1.7
	elif(nome == "LIQUIDIFICADOR"):
		quantidade = peso*1.8
	elif(nome == "MICROONDAS"):
		quantidade = peso*15
	elif(nome == "NOTEBOOK"):
		quantidade = peso*2.5
	elif(nome == "TELEVISOR"):
		quantidade = peso*15
	else:
		quantidade = peso*2.4
		nome == "VENTILADOR"
	print(float(round(quantidade, 2)))