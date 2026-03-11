x = int(input())
x1 = x // 10000
x2 = x % 10000
p=(x1 + x2) ** 2

if x == p:
	print(x,"atende a propriedade")
else:
	print(p)