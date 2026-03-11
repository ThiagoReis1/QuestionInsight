# faça seu código aqui!
distancia = int(input("Insira a distancia em km: "))
taxa = 50

if distancia < 10:
	total = taxa + 5.50
	print(round(total, 2))
elif distancia == 10:
	total = taxa + 7.75
	print(round(total, 2))
elif distancia > 10:
	total = taxa + 10
	print(round(total, 2))