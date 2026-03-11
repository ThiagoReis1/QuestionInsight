# faça seu código aqui!
x = int(input("Qtde de pizzas: "))
pb = 5.0

if x < 3:
	total = x * pb + 3.0
elif x == 3:
	total = x * pb + 3.25
elif x > 3:
	total = x * pb + 4.50

print(round(total, 2))