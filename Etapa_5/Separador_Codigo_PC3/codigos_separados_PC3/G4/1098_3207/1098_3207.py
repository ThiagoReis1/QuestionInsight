n = int(input())
a = n//1000
e = n%1000
c = (a-e)**4
if (n==c):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")