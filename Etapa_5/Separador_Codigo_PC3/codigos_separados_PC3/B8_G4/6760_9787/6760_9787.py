qp = float(input("Quantidade de pecas: "))

if qp < 10:
	taxa = 3.25 + 30
elif qp == 10:
	taxa = 4.50 + 30
elif qp > 10:
	taxa = 6 + 30
print(round(taxa, 2))
