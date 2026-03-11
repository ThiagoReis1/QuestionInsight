pecas = int(input("Quantidade de pecas de roupa para lavar: "))
if pecas < 10:
	total = 30 + 3.25
	print(round(total,2))
elif pecas == 10:
	total = 30 + 4.50
	print(round(total,2))
else:
	total = 30 + 6
	print(round(total,2))