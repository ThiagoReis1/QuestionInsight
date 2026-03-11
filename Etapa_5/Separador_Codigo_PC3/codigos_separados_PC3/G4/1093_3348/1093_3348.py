n1 = int(input())
a1 = n1 // 100
a2 = n1 % 100
c = a1**2 + a2**2
if (c == n1):
	print("atende")
	print(n1)
else:
	print("nao atende")
	print(n1)