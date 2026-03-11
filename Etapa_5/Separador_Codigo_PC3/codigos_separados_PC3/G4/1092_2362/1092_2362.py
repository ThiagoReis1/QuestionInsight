n = int(input(":"))

n1 = n // 100
rn1 = n % 100
n2 = rn1 // 10
rn2 = rn1 % 10

formula = (n1**3) + (n2**3) + (rn2**3)

if (formula == n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")
	
