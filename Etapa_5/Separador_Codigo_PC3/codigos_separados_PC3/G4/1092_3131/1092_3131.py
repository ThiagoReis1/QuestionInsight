n = int(input("Numero fornecido: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

n1 = (a ** 3) + (b ** 3) + (c ** 3)

if (n == n1):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")