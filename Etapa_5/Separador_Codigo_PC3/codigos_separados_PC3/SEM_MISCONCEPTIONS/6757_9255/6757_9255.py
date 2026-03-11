quant = int(input("Pizzas encomendadas: "))
pizza = 5

if quant < 3:
	taxa = (quant * pizza) + 3
	print(round(taxa, 2))
elif quant == 3:
	taxa = (quant * pizza) + 3.25
	print(round(taxa, 2))
else:
	taxa = (quant * pizza) + 4.5
	print(round(taxa, 2))
	


