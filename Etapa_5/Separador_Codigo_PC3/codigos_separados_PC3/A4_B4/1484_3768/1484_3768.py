N = input("digite o nome do equipamento:").upper()
C = int(input("digite a capacidade de carga:"))

if (C < 0 or C > 1000):
	print("Entrada invalida")
elif (N == "COMPUTADOR"):
	print(C//12)
elif (N == "FREEZER"):
	print = (C//52)
elif (N == "FURADEIRA"):
	print(C//1.7)
elif (N == "LIQUIDIFICADOR"):
	print(C//1.8)
elif (N == "MICROONDAS"):
	print(C//15)
elif (N == "NOTEBOOK"):
	print(C//2.5)
elif (N == "TELEVISOR"):
	print(C//15)
elif (N == "VENTILADOR"):
	print(C//2.4)
else:
	print("Entrada invalida")
	
