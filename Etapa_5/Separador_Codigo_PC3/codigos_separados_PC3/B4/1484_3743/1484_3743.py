nome = input().upper()
capacidade = int(input())
if capacidade  < 0 or capacidade > 1000:
	print("Entrada invalida")
elif nome == "COMPUTADOR" :
	print(int(capacidade / 12))
elif nome == "FREEZER":
	print(int(capacidade / 52))
elif nome == "FURADEIRA":
	print(int(capacidade / 1.7))
elif nome == "LIQUIDIFICADOR":
	print(int(capacidade / 1.8))
elif nome == "MICROONDAS":
	print(int(capacidade / 15))
elif nome == "NOTEBOOK":
	print(int(capacidade / 2.5))
elif nome == "TELEVISOR":
	print(int(capacidade / 15))
elif nome == "VENTILADOR":
	print(int(capacidade / 2.4))
else:
	print("Entrada invalida")
