n=int(input("numero fornecido:"))
n1=n//100
r1=n%100
if(n==(n1+r1)**2):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")