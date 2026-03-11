# Entrada

consumo = int(input("Consumo de energia:"))

# Condicao

if (consumo < 100):
	total = (0.50 * consumo) + 50
	print(round(total,2))
elif (consumo < 250):
	total = (0.75 * consumo) + 50
	print(round(total,2))
elif (consumo < 500):
	total = (1 * consumo) + 50
	print(round(total,2))
else:
	total = (1.25 * consumo) + 50
	print(round(total,2))


