n = int(input("Digite o numero:"))

n1 = n // 1000
n2 = n % 1000

if ((n1 + n2) ** 2 == n):
	m = "atende"
	n = n
else:
	m = "nao atende"
	
print(m)
print(n)