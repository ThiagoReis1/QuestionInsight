valor= float(input("Digite o valor total da compra:"))
cod= input("D, P ou C:")

if cod == "D" or cod == "P":
	total= valor - (13/100 * valor)
	print(round(total, 2))
elif cod == "C":
	entradas= int(input("1 ou 2:"))
	if entradas == 1:
		total= valor
		print(round(total,2))
	elif entradas == 2:
		total = valor + (8/100 * valor)
		print(round(total, 2))

