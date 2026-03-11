n = int(input())

n2 = n%100
n1 = n//100
prop = n1**2 + n2**2

if n == prop:
	print(n, "atende a propriedade")
else:
	print(int(prop))
	