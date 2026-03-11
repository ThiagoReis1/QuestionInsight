n = int(input("Insira um numero: "))
p1 = n % 10000

p2 = n // 10000

variavel = (p1 + p2) ** 2
if (variavel == n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")
