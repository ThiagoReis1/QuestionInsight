# faça seu código aqui!
quant = int(input("Digite a quantidade de pizzas: "))
tax = 5.00


if quant < 3:
	total = (quant * 3) + tax
	print(round(total, 2))
	
elif quant == 3:
	total = (quant * 3.25) + tax
	print(round(total, 2))
	
elif quant > 3:
	total = (quant * 4.50) + tax
	print(round(total, 2))
