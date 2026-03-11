n=int(input("Digite um numero:"))
n1=n//100
n2=n%100
if(n==( (n1**2)+(n2**2) ) ):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)