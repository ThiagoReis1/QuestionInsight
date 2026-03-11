n = int(input("Numero: "))
n1 = n // 100
n2 = n % 100
if (n == (n1 + n2) ** 2):
	m = "atende"
else:
	m = "nao atende"
print(n)
print(m)