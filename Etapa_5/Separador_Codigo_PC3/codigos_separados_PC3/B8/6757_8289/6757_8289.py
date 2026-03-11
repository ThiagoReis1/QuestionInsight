# faça seu código aqui!

pizza = int(input(":"))

entrega = 5

if pizza < 3:
	total = (pizza * entrega) + 3.0
elif pizza == 3:
	total = (pizza * entrega) + 3.25
elif pizza > 3:
	total = (pizza * entrega) + 4.5


print(round(total,2))