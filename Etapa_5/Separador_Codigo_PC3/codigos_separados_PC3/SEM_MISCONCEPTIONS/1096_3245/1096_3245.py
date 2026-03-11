n = int(input())

a = n // 10000
rest_a = n % 10000
b = rest_a // 100
rest_b = rest_a % 100
c = rest_b // 1

valor = a**3 + b**3 + c**3

if(valor == n):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)

