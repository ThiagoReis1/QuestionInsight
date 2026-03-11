l1 = int(input("leia o nmr de pizzas encomendas:"))

if (l1 < 3):
	taxa = 5 * l1
	total = taxa + 3
elif (l1 == 3):
	taxa = 5 * l1
	total = taxa + 3.25
elif (l1 > 3):
	taxa = 5 * l1
	total = taxa + 4.50
print("total=",round(total,2))

