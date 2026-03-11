# faça seu código aqui!
quantidade = int(input("Digite a quantidade de pecas de roupa: "))
fixo = 30.00
if quantidade < 10:
	taxa = 3.25
	total = fixo + taxa
	print(round(total, 2))
elif quantidade == 10:
	taxa = 4.50
	total = fixo + taxa
	print(round(total, 2))
elif quantidade > 10:
	taxa = 6.00
	total = fixo + taxa
	print(round(total, 2))