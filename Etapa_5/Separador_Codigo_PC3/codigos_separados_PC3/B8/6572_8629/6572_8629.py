# faça seu código aqui!
n = int(input("numero de pizzas: "))
entrega = 5

if (n < 3):
	taxa = 3
	total = (n * entrega) + taxa
	print("total=" ,round(total,2))
elif (n == 3):
	taxa = 3.25
	total = (n * entrega) + taxa
	print("total=" , round(total,2))
elif (n > 3):
	taxa = 4.50
	total = (n * entrega) + taxa	
	print("total=", round(total,2))