food = input("Quantidade de comida(L/P): ")
quantidade = int(input("Quantidade: "))
quantidade2 = int(input("Quantidade de refrigerante: "))

if food == "L":
	total1 = quantidade * 6.00 + quantidade2 * 3.00
	print(round(total1, 2))
else:
	total2 = quantidade * 4.50 + quantidade2 * 3.00
	print(round(total2, 2))