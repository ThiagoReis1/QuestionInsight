x = input("Digite o nome: ").lower()
y = float(input("Quantidade de equipamento : "))
(y)
if(x =="COMPUTADOR".lower()):
	print(round(( y * 12),2))
elif(x == "FREEZER".lower()):
	print(round((y * 52),2))
elif(x == "FURADEIRA".lower()):
	print(round((y * 1.7),2))
elif(x == "LIQUIDIFICADOR".lower()):
	print(round((y * 1.8),2))
elif(x == "MICROONDAS".lower()):
	print(round((y * 15),2))
elif(x =="NOTEBOOK".lower()):
	print(round((y * 2.5),2))
elif(x == "TELEVISOR".lower()):
	print(round((y * 15),2))
elif(x == "VENTILADOR".lower()):
	print(round((y * 2.4),2))
else:
	print("Entrada invalida")