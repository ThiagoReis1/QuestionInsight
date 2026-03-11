# faça seu código aqui!

a = int(input("Digite a quantitdade de pizzas: "))

if (a < 3):
	b = 5 * a
	t = b + 3
	print("total= ", round(t, 2))
	
elif (a == 3):
	b = 5 * a
	t = b + 3.25
	print("total= ", round (t, 2))
elif (a > 3):
	b = 5 * a
	t = b + 4.5
	print("total= ", round (t, 2))