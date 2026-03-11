pizza = int(input("Pizzas"))
if pizza < 3:
	caso1 = pizza * 5 + 3
	print(caso1)
elif pizza == 3:
	caso2 = pizza * 5 + 3.25
	print(caso2)
elif pizza > 3:
	caso3 = pizza * 5 + 4.50
	print(caso3)