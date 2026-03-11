qtde_pizzas = int(input())

if qtde_pizzas < 3:
	total = 5 * qtde_pizzas + 3
	print("total=", round(total, 2))
if qtde_pizzas == 3:
	total = 5 * qtde_pizzas + 3.25
	print("total=",round(total, 2))
if qtde_pizzas > 3:
	total = 5 * qtde_pizzas + 4.50
	print("total=", round(total, 2))