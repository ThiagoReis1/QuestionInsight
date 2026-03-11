total = float(input("total de compra: "))
cod = input("D, P, C1, C2: ")

if cod == "D" or cod == "P":
	desconto = 0.12
	valor = total - (total * desconto)
	print(round(valor, 2))
elif cod == "C1":
	print(round(total, 2))
else:
	valor2 = (total * 7/100) + total
	print(round(valor2, 2))
	