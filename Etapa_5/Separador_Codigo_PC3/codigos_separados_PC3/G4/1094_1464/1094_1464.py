
n=int(input("n:"))
n1=n//1000
n2=n%1000
div=(n1+n2)**2

if(n==div):
	print("X atende a propriedade")
else:
	print(div)
