n = int(input("n:"))
n1 = n//10000
n2 = n%10000
n3 = (n1+n2)**2
if(n==n3):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")

	