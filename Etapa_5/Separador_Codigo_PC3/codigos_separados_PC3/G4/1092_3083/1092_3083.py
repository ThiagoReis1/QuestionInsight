n = int(input("numero "))

n1 = n // 100
rn1 = n % 100
n2 = rn1 // 10
n3 = rn1 % 10

if(n == n1 ** 3 + n2 ** 3 + n3 ** 3):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")