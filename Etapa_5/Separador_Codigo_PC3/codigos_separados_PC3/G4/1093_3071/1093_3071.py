n = int(input("Digite: "))
a = n // 100
b = (n % 100)
q = (a ** 2) + (b ** 2)
if (n == q):
	print( "atende" )
	print(n)
else: 
	print( "nao atende" )
	print(n)
