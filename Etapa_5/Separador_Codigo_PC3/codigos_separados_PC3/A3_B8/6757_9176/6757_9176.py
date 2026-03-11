entrega = 5
pizza = int(input("Digite a quantidade de pizzas: "))
if pizza > 0 and pizza < 3:
 total = float(pizza * 5 + 3)
 print(round(total, 2))
elif pizza == 3:
 total = pizza * 5 + 3.25
 print(round(total, 2))
elif pizza > 3:
 total = pizza * 5 + 4.5
 print(round(total, 2))