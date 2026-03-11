n = int(input("numero: "))
x = n // 10000
y = n % 10000
k = (x + y)**2
if( n == k ):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")