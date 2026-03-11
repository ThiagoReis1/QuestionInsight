# faça seu código aqui!
pizzas = int(input("Digite o numero de pizzas encomendadas:"))

if pizzas < 3:
	total = pizzas * 5 + 3 
	print("total=",round(total,2))
elif pizzas == 3:
	total = pizzas * 5 + 3.25
	print("total=",round(total,2))
elif pizzas > 3:
	total = pizzas * 5 + 4.50
	print("total=",(round(total,2)))