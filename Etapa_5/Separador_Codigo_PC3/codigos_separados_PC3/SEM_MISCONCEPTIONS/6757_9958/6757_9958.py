n_pizzas = int(input("numero de pizzas"))

if n_pizzas < 3:
	total = n_pizzas*5+3.0
elif n_pizzas == 3:
	total = n_pizzas*5+3.25
else:
	total = n_pizzas*5+4.5

print(round(total,2))