n = int(input("Insira um numero: "))
x = n // 10000
y = n % 10000
print(n)

if (((x + y) ** 2) == n):
	print("atende")
else:
	print("nao atende")
