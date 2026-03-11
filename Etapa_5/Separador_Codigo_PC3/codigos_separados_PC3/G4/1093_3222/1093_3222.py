x = int(input("numero: "))

d1 = x // 100
d2 = x % 100


c = (d1 **2) + (d2 ** 2)

if (x == c):
	print("atende")
	print(x)
else:
	print("nao atende")
	print(x)

