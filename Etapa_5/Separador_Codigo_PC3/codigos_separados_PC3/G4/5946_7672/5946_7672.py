Lanche = input("L ou P: ")
var1 = int(input("quantidade de lanches ou pizzas: "))
var2 = float(input("quantidade de refrigerantes: "))

if (Lanche == "L"):
	vt = var1 * 6 + var2 * 3
else:
	vt = var1 * 4.50 + var2 * 3
print(round(vt, 1))