n = int(input("Digite seu numero: "))
n1 = n //1000
n2 = n % 1000
n3 = (n1 - n2)**4
if ( n == n3):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")