quantidade = int(input("quantidade de pecas de roupa para a lavagem"))
if quantidade < 10 :
	total = 3.25 + 30
	print(total)
elif quantidade == 10 :
	total = 4.50 + 30
	print(total)
elif quantidade > 10 :
	total = 6 + 30
	print(total)