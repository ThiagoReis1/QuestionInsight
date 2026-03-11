n = int(input("Digite o número X:"))
	
p1 = n % 100
p2 = n // 100

if ((p1 + p2)**2 == n):
	print(n, "atende a propriedade")
	
else:
	print((p1 + p2)**2)
		
