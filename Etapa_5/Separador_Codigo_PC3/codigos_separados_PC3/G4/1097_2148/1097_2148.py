n = int(input("numero fornecido: "))
n1 = n // 1000
r1 = n % 1000

if(n==(n1-r1)**2):
	print("atende")
	print(n)
	
	
else:
	print("nao atende")
	print(n)
	