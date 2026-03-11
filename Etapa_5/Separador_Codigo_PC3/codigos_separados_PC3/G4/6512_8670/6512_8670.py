# faça seu código aqui!

dd = int(input("Quantidade de duplas deliciosas pedidas por um cliente: "))


if (dd > 3):
	x = dd * 32.90
	z = x - (x * 0.20)
	print(round(z, 2))
	
else:
	y = dd * 32.9
	print(round(y, 2))