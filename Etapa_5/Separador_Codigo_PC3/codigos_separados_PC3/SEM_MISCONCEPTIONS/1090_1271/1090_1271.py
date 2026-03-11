c_1 = float(input("Digite o valor: "))
c_2 = float(input("Digite o valor: "))
c_3 = float(input("Digite o valor: "))
c_4 = float(input("Digite o valor: "))
limite = float(input("Digite o valor: "))

if (c_1 + c_2 + c_3 + c_4 <= limite):
	total = c_1 + c_2 + c_3 + c_4 
	print(round(total,2))
	print("Sim")
else:
	total = c_1 + c_2 + c_3 + c_4 
	print(round(total,2))
	print("Nao")