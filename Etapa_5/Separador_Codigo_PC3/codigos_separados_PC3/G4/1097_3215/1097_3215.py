x = int(input())

x1 = x // 1000
y = x % 1000

if ((x1 - y)**2 == x):
	print("atende")
	print(x)
else:
	print("nao atende")
	print(x)
