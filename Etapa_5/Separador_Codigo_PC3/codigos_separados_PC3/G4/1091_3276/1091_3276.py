n=int(input("numero"))
d2=(n//100)%100
d4=n%100

if((d2+d4)**2 == n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")