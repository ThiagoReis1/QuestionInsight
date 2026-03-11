a=int(input())
b=int(input())
k=(a - b)**2
x= (a**2 - 2*a*b + b**2)
if(x==k):
	print(x,"atende a propriedade")
else:
	print(x)