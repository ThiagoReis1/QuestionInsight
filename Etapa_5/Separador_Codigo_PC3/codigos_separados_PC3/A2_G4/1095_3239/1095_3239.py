x = int(input("Digite o numero:"))

a1 = x // 10000
a2 = x % 10000

if ((a1 + a2) ** 2 == x):
	p = "atende"
	x = x
else:
	p = "nao atende"
	
print(x)
print(p)

