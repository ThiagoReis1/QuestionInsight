x=int(input())

n1=x//10000
r1=x%10000

a=(n1+r1)**2


if(x==a):
	print(x)
	print("atende")
else:
	print(x)
	print("nao atende")