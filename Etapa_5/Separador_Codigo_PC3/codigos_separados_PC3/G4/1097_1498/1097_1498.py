n = int(input("digite o valor: "))
n1 = n // 1000
n2 = n % 1000
x = ((n1 - n2) ** 2)
if (x == n):
	print(x,"atende a propriedade")
else:
	print(x)
