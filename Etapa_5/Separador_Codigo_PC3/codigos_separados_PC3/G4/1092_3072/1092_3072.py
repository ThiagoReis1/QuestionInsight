n = int(input("insira um numero: "))

x = n // 1000
y = n % 1000
z = n // 1000 

if	(((x) ** 3) + ((y) ** 3) + ((z) ** 3)  == n):
	print("atende")
	
else:
	print("nao atende")