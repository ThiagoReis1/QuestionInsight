cenouras = int(input("Numero de cenouras compradas: "))

if (cenouras < 5):
	preco = 1.20
	total = cenouras * preco
	print(round(total, 2))
else:
	preco = 0.90
	total = cenouras * preco
	print(round(total, 2))