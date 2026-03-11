n = int(input("Numero (6 digitos):"))
i3 = n // 1000
u3 = n % 1000
if( (i3-u3)**4 == n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")	