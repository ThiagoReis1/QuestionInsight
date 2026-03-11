x = int(input("Digite o valor:"))
x1 = x // 10000
resto_x1 = x % 10000
x2 = resto_x1 // 100
resto_x2 = resto_x1 % 100
x3 = resto_x2

y = (x1) ** 3 + (x2) ** 3 + (x3) ** 3

if ( x == y ):
	print(x, "atende a propriedade")
else:
	print(y)