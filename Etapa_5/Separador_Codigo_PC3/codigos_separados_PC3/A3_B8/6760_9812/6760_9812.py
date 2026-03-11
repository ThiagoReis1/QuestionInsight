# faça seu código aqui!
pecas = int(input("Quantidade de pecas: "))

total = 0

if pecas < 10:
	total = 30 + 3.25
	print(round(total,2))
	
elif pecas == 10:
	total = 30 + 4.5
	print(round(total,2))

elif pecas > 10:
	total = 30 + 6
	print(round(total,2))