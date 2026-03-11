n = int(input())

n1 = n // 1000
n2 = n % 1000

p = (n1 + n2) ** 2
if (p == n):
	print("atende")
else:
	print("nao atende")
print(n)