n = int(input("n:  "))
a = n // 100
b = n % 100
c = a**2 + b**2
if (n != c):
	print("nao atende")
	print(n)
else: 
	print("atende")
	print(n)
